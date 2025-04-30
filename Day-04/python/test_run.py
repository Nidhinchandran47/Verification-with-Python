import os
import cocotb_test.simulator

def test_counter():
    verilog_sources = ["../rtl/counter.v"]
    os.environ["WIDTH"] = "4"
    parameters = {"WIDTH":4}

    extra_compile_args = []
    if os.getenv("WAVE", "0") == "1":
        extra_compile_args.append("-DDUMP_ENABLED")

    cocotb_test.simulator.run(
        verilog_sources=verilog_sources,
        toplevel="counter", 
        module="counter_tb", 
        sim_build="sim_build", 
        compile_args=extra_compile_args,
        parameters=parameters,
    )

if __name__ == "__main__":
    test_counter()
