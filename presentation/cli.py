import argparse
import json
from application.bootstrap import build_system, make_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Command Pattern Demo (Cart)")
    parser.add_argument(
        "--cmds",
        type=str,
        required=True,
        help='JSON list of commands, e.g. '
             '[{"type":"add","sku":"A","qty":2,"unit_price":10.0},'
             '{"type":"percent","percent":10},'
             '{"type":"remove","sku":"A","qty":1}]'
    )
    parser.add_argument("--undo", type=int, default=0, help="Undo last N commands")
    parser.add_argument("--redo", type=int, default=0, help="Redo last N commands")
    args = parser.parse_args()

    cart, invoker = build_system()
    specs = json.loads(args.cmds)

    for spec in specs:
        cmd = make_command(cart, spec)
        invoker.run(cmd)

    if args.undo:
        invoker.undo(args.undo)
    if args.redo:
        invoker.redo(args.redo)

    print("Items:")
    for sku, (qty, price) in cart.items().items():
        print(f" - {sku}: qty={qty}, unit_price={price:.2f}")
    print(f"Discount: {cart.discount_percent:.1f}%")
    print(f"Subtotal: {cart.subtotal():.2f}")
    print(f"Total: {cart.total():.2f}")


if __name__ == "__main__":
    main()
