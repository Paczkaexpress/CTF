.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp ; function initialisation
	mov	ebp,esp ; function initialisation
	mov	eax,DWORD PTR [ebp+0x8] ; accesing the first argument
	mov	ebx,DWORD PTR [ebp+0xc] ; accesing the second argument
	mov	eax,ebx ; moving the value of the ebx register to the abx
	mov	esp,ebp
	pop	ebp	
	ret
