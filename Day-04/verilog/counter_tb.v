module counter_tb ();
    reg clk;
    reg reset;
    reg enable;
    reg mode;
    reg load;
    reg [3:0] load_value;
    wire [3:0] count;
    wire terminal_count;

    counter #(
    .WIDTH             (4)
) u_counter (
    .clk               (clk),
    .reset             (reset),
    .enable            (enable),
    .mode              (mode),
    .load              (load),
    .load_value        (load_value),
    .count             (count),
    .terminal_count    (terminal_count)
);
    always
        #5 clk = ~clk;
    initial begin
        clk = 0;
        reset = 0;
        enable = 0;
        mode = 0;
        load = 0;
        load_value = 4'b0000;

        #10;
        reset = 1;
        #10;
        reset = 0;
        #10;
        enable = 1;
        #50;
        mode = 1;
        #70;
        enable = 0;
        mode = 0;
        #10;
        enable = 1;
        #100;
        load_value = 4'b1110;
        load = 1;
        #20;
        load = 0;
        #100;
        $finish;
    end

    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, counter_tb);
    end

endmodule
