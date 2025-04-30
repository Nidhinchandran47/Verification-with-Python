# Top level settings
FNAME             ?= counter
VCD_FILE          ?= dump.vcd
VERILOG_SOURCE     = ../rtl/$(FNAME).v
SV_TESTBENCH       = ../verilog/$(FNAME)_tb.v
PYTHON_PATH        = ../python
TOPLEVEL           = $(FNAME)
MODULE             = $(FNAME)_tb
TOPLEVEL_LANG     ?= verilog
SIM               ?= icarus
WAVE              ?= False
WIDTH             ?= 4



ifeq ($(WAVE),True)
  DUMP_DEFINE = -DDUMP_ENABLED
else
  DUMP_DEFINE =
endif

help:
	@echo "\033[1;34mMakefile for $(MODULE)\033[0m"
	@echo "\033[1;32mUsage:\033[0m"
	@echo "  \033[1;33mmake clean\033[0m                - Clean up generated files"
	@echo "  \033[1;33mmake cocotb\033[0m               - Run cocotb Python testbench"
	@echo "  \033[1;33mmake cocotb WAVE=True\033[0m     - Run with waveform dump"
	@echo "  \033[1;33mmake sv\033[0m                   - Run SystemVerilog testbench"
	@echo "  \033[1;33mmake wave\033[0m                 - Open GTKWave to view waveform"
	@echo "\033[1;32mOptions:\033[0m"
	@echo "  \033[1;36mFNAME=<design_name>\033[0m        - Specify top module name"
	@echo "  \033[1;36mVCD_FILE=<vcd_file_name>\033[0m  - Specify VCD file (default: dump.vcd)"

cocotb:
	@echo "Running cocotb testbench..."
	PYTHONPATH=$(PYTHON_PATH) \
	$(MAKE) -f $(shell cocotb-config --makefiles)/Makefile.sim \
		SIM=$(SIM) \
		TOPLEVEL_LANG=$(TOPLEVEL_LANG) \
		TOPLEVEL=$(TOPLEVEL) \
		MODULE=$(MODULE) \
		VERILOG_SOURCES="$(abspath $(VERILOG_SOURCE))" \
		PARAMETERS="$(PARAMETERS)" \
		COMPILE_ARGS="$(DUMP_DEFINE) -P$(TOPLEVEL).WIDTH=$(WIDTH)"

sv:
	@echo "Running SystemVerilog testbench..."
	iverilog -o simv $(VERILOG_SOURCE) $(SV_TESTBENCH) 
	vvp simv

wave:
	@echo "Opening GTKWave..."
	@if [ -f "$(FNAME).vcd" ]; then \
	 	gtkwave $(FNAME).vcd & \
	else \
		gtkwave $(VCD_FILE) & \
	fi

clean:
	rm -rf simv *.vcd *.xml *.f *.log *.out __pycache__ test/__pycache__ *.fst sim_build

.PHONY: cocotb sv wave clean help
