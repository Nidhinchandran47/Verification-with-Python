`timescale 1ns/1ps
module counter #(
    parameter WIDTH = 4
) (
    input clk,
    input reset,
    input enable,
    input mode,
    input load,
    input [WIDTH-1:0] load_value,
    output reg [WIDTH-1:0] count,
    output reg terminal_count
);
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            count <= 0;
            terminal_count <= 0;
        end
        else if (enable) begin
            if (load) begin
                count <= load_value;
                terminal_count <= 0;
            end
            else if (mode) begin
                if (count == 0) begin
                    terminal_count <= 1;
                    count <= (1 << WIDTH) - 1;
                end
                else begin
                    count <= count - 1;
                    terminal_count <= 0;
                end
            end
            else begin
                if (count == (1 << WIDTH) - 1) begin
                    terminal_count <= 1;
                    count <= 0;
                end
                else begin
                    count <= count + 1;
                    terminal_count <= 0;
                end
            end
        end
    end

    `ifdef DUMP_ENABLED
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, counter);
    end
    `endif

endmodule
