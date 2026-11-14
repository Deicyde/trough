---
declaration: lemma
origin: cited
lean: MIPRE.Cost.recursive_compression_halting, MIPRE.Cost.compressibility_criterion_halting
statement: formalized
proof: formalized
---

# Halting form of the two reduction lemmas

Lemma [Recursive compression](lem-recursive-compression.md) and Lemma [Compressibility criterion](lem-compressible-criterion.md) both hold with the halting problem taken in the ambient formalization's own form: the reduction may be presented as a computable map defined on the codes of a fixed Gödel numbering of the partial recursive functions, halting being halting of the code on input $0$, rather than on the programs of the cost model in which the two lemmas are proved.

## Depends on

- [Recursive compression](lem-recursive-compression.md)
- [Compressibility criterion](lem-compressible-criterion.md)

## Proof

Compose the reduction with a compiler from codes to programs of the cost model that is computable on descriptions and preserves halting on the empty input: hardcode the code's index into a fixed program for the universal partial function, which exists because that partial function is partial recursive, and observe that the description of the result is a fixed primitive recursive tree around the index. Only the interface changes; neither lemma's content is touched, and the compiler carries no time bound, which is why this step is available for the computable version of the main theorem and not for the polynomial-time one.

## Lean

Formalized as [`MIPRE.Cost.recursive_compression_halting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.recursive_compression_halting), [`MIPRE.Cost.compressibility_criterion_halting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.compressibility_criterion_halting).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 463](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L463)
