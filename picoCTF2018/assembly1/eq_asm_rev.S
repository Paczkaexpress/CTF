.intel_syntax noprefix
.bits 32
	
.global asm1

asm1:
	push	ebp ; 
	mov	ebp,esp ; software preabule
	cmp	DWORD PTR [ebp+0x8],0x98 ; compare input with the 0x98, basicaly it do 0x76 - 0x98 = 30?
	jg 	part_a	; jump if 0x76 is greater 
	cmp	DWORD PTR [ebp+0x8],0x8 ; compare input with the 0x8, 0x76-0x08 = 0x6E
	jne	part_b ; jump if not equal 
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x16
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b: ; jump from main
	mov	eax,DWORD PTR [ebp+0x8] ; move 0x76 to eax register
	sub	eax,0x3 ; substract 3 = 0x76 - 0x03 = 0x73
	jmp	part_d ; jump to the part d
	cmp	DWORD PTR [ebp+0x8],0xbc
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp ; return and quit
	ret


