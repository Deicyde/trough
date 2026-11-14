---
declaration: theorem
origin: cited
lean: book.quadratic_reciprocity.fermat_little
statement: formalized
---

# Fermat's little theorem

For $a \not\equiv 0 \pmod{p}$,

$$
a^{p - 1} \equiv 1 \pmod{p}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $\mathbb{Z}_p^* = \mathbb{Z}_p \setminus \{0\}$ is a group with multiplication, the set $\{1a, 2a, 3a, \dots, (p-1)a\}$ runs again through all nonzero residues,

$$
(1a)(2a)\dots((p-1)a) \equiv 1\cdot 2 \cdots (p-1) \pmod{p}
$$

and hence by dividing by $(p - 1)!$, we get $a^{p - 1} \equiv 1 \pmod{p}$.

## Lean

Stated as [`book.quadratic_reciprocity.fermat_little`](https://mo271.github.io/FormalBook/docs/find/#doc/book.quadratic_reciprocity.fermat_little); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter05.tex, line 4](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter05.tex#L4)
