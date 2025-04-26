import os
from cocotb_test.simulator import run

def test_and_gate():
    run(
        verilog_sources=["../rtl/and_gate.v"],
        toplevel="and_gate",
        module="and_gate_tb",                      
        toplevel_lang="verilog",
        python_search=["../python"]
    )

test_and_gate()
