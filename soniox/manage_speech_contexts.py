import sys
import argparse
import json
from google.protobuf.json_format import MessageToDict
from soniox.speech_service import SpeechClient
from soniox.speech_service_pb2 import (
    SpeechContext,
    SpeechContextEntry,
    CreateSpeechContextRequest,
    DeleteSpeechContextRequest,
    ListSpeechContextNamesRequest,
    GetSpeechContextRequest,
    UpdateSpeechContextRequest,
)


def pb_to_dict(pb):
    return MessageToDict(pb, including_default_value_fields=True, preserving_proto_field_name=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="List names of speech contexts.")
    parser.add_argument("--get", action="store_true", help="Get speech context (specify --name).")
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create speech context (specify --name, --phrases/--phrases_fn, --boost).",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update speech context (specify --name, --phrases/--phrases_fn, --boost).",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete speech context (specify --name).",
    )
    parser.add_argument("--name", type=str, help="Speech context name.")
    parser.add_argument("--phrases", type=str, help="Phrases separated by semicolon.")
    parser.add_argument("--phrases_fn", type=str, help="File containing phrases on separate lines.")
    parser.add_argument("--boost", type=float, help="Speech context name.")
    args = parser.parse_args()

    num_commands = args.list + args.get + args.create + args.update + args.delete
    if num_commands == 0:
        parser.print_help()
        sys.exit(0)
    if num_commands > 1:
        print("Incorrect usage: more than one command specified.", file=sys.stderr)
        sys.exit(1)

    with SpeechClient() as client:
        if args.list:
            print("Listing names of speech contexts.")

            response = client.service_stub.ListSpeechContextNames(
                ListSpeechContextNamesRequest(
                    api_key=client.api_key,
                )
            )

            if len(response.names) == 0:
                print("(no speech contexts)")
            else:
                for name in response.names:
                    print(f"  {name}")

        elif args.get:
            if args.name is None:
                print(f"Incorrect usage: --get requires --name.", file=sys.stderr)
                sys.exit(1)

            print(f'Getting speech context "{args.name}".')

            response = client.service_stub.GetSpeechContext(
                GetSpeechContextRequest(
                    api_key=client.api_key,
                    name=args.name,
                )
            )

            print("Speech context:")
            print(json.dumps(pb_to_dict(response.speech_context), indent=2))

        elif args.create or args.update:
            cmd = "--create" if args.create else "--update"

            if args.name is None:
                print(f"Incorrect usage: {cmd} requires --name.", file=sys.stderr)
                sys.exit(1)

            if args.phrases is not None and args.phrases_fn is not None:
                print(
                    "Error: --phrases and --phrases_fn must not both be specified.",
                    file=sys.stderr,
                )
                sys.exit(1)

            if args.phrases is not None:
                phrases = args.phrases.split(";")
            elif args.phrases_fn is not None:
                with open(args.phrases_fn, "r") as fh:
                    phrases = list(fh)
            else:
                print(
                    f"Incorrect usage: {cmd} requires --phrases or --phrases_fn.", file=sys.stderr
                )
                sys.exit(1)

            phrases = [phrase.strip() for phrase in phrases]
            phrases = [phrase for phrase in phrases if phrase != ""]

            if args.boost is None:
                print(f"Incorrect usage: {cmd} requires --boost.", file=sys.stderr)
                sys.exit(1)

            speech_context = SpeechContext(
                entries=[
                    SpeechContextEntry(
                        phrases=phrases,
                        boost=args.boost,
                    )
                ],
                name=args.name,
            )

            if args.create:
                print(f'Creating speech context "{args.name}".')

                client.service_stub.CreateSpeechContext(
                    CreateSpeechContextRequest(
                        api_key=client.api_key,
                        speech_context=speech_context,
                    )
                )
            else:
                print(f'Updating speech context "{args.name}".')

                client.service_stub.UpdateSpeechContext(
                    UpdateSpeechContextRequest(
                        api_key=client.api_key,
                        speech_context=speech_context,
                    )
                )

        elif args.delete:
            if args.name is None:
                print("Incorrect usage: --delete requires --name.", file=sys.stderr)
                sys.exit(1)

            print(f'Deleting speech context "{args.name}".')

            client.service_stub.DeleteSpeechContext(
                DeleteSpeechContextRequest(
                    api_key=client.api_key,
                    name=args.name,
                )
            )


if __name__ == "__main__":
    main()
