---
declaration: corollary
origin: cited
lean: IsDedekindDomain.linearEquivTensorProductModule
statement: formalized
proof: formalized
---

# IsDedekindDomain.AKLB.tensorProduct_module_algEquiv

If $M$ is any $K$-module then the canonical map $B\otimes_A M\to L\otimes_K M$ is an isomorphism.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We can factor this map as $B\otimes_AM\cong B\otimes_A(K\otimes_KM)\cong (B\otimes_A K)\cong_KM\to L\otimes_KM$ and we just showed that the latter map was an isomorphism.

## Lean

Formalized as [`IsDedekindDomain.linearEquivTensorProductModule`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.linearEquivTensorProductModule).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 482](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L482)
