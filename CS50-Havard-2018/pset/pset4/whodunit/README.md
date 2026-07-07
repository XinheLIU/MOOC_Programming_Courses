# Questions

## What's `stdint.h`?

A header file for a C standard library that allow programmers to write more portable code by providing a set of typedefs that specify exact-width integer types (together with max and min values).

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

It means you want to use the data in the exact specified storage length and exact type. For example, unit_8 means unsigned 8-bit length int.

There are a lot of situations a programmer might want to do that: For example, reading a bitmap file where the type, size, and layout of a file that contains a DIB.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE = 8 bits = 1 byte
DWORD= 32 bits = 4 bytes
LONG = 32 bits = 4 bytes
WORD = 16 bits = 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

0x424d (BM for ACSII)

## What's the difference between `bfSize` and `biSize`?

`bfSize` is the number of bytes in the file.
`biSize` is the number of bytes in the info header.

## What does it mean if `biHeight` is negative?

The height of the bitmap, in pixels. If biHeight is positive, the bitmap is a bottom-up DIB and its origin is the lower-left corner.
If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

The file it tries to open does not exist or requires a permission to open.

## Why is the third argument to `fread` always `1` in our code?

It tries to read one RGB pixel at a time.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3.

## What does `fseek` do?

skip over the padding and to the next RGB triple.


## What is `SEEK_CUR`?

The current position of the file pointer. (the current position we are in reading the file).
