#!/usr/bin/python


from bcc import BPF

text = """
int kprobe__sys_clone(void *ctx) {
    bpf_trace_printk("Hello World!\\n");
    return 0;
}
"""

BPF(text=text).trace_print()
