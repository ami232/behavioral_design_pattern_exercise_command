import sys
from importlib import reload
import presentation.cli as cli


def run_cli(args_list, capsys):
    backup = sys.argv
    try:
        sys.argv = ["prog"] + args_list
        reload(cli)
        cli.main()
        return capsys.readouterr().out
    finally:
        sys.argv = backup


def test_cli_flow_with_undo_redo(capsys):
    cmds = '[{"type":"add","sku":"A","qty":2,"unit_price":10.0},{"type":"add","sku":"B","qty":5,"unit_price":3.0},{"type":"percent","percent":10},{"type":"remove","sku":"B","qty":2}]'
    out = run_cli(["--cmds", cmds, "--undo", "2", "--redo", "2"], capsys)

    assert "Items:" in out
    assert "A: qty=2, unit_price=10.00" in out
    assert "B: qty=3, unit_price=3.00" in out
    assert "Discount: 10.0%" in out
    assert "Subtotal: 29.00" in out
    assert "Total: 26.10" in out
