`timescale 1ns / 1ps
module d_ff (
    input clk,
    input reset,  // active low reset
    input d,
    output reg q
);
    always @(posedge clk or negedge reset) begin
        if (!reset) begin
            q <= 1'b0;
        end else begin
            q <= d;
        end
    end

    `ifdef DUMP_ENABLED
        initial begin
            $dumpfile("dump.vcd");
            $dumpvars(0, d_ff);
        end
    `endif

endmodule
