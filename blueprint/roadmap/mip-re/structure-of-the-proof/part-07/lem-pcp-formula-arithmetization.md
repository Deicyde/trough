---
declaration: lemma
origin: cited
lean: MIPRE.SAT.Fml.eval_arith, MIPRE.SAT.Fml.degreeOf_arith_le
statement: formalized
proof: formalized
---

# Formula arithmetization and occurrence bounds

A Boolean formula has a polynomial arithmetization over any nontrivial commutative ring, agreeing with its Boolean value on Boolean inputs. The degree in each variable is at most the number of occurrences of that variable, including identifications made by the assignment of formula inputs to polynomial variables.

## Depends on

- [The low-degree code](def-ld-encoding.md)

## Proof

Replace conjunction by multiplication, negation by subtraction from one, and disjunction of $f,g$ by $1-(1-f)(1-g)$. Induction on the formula proves both claims. The circuit application must bound external input occurrences as well as gate fan-out; the current circuit well-formedness predicate only bounds the latter.

## Lean

Formalized as [`MIPRE.SAT.Fml.eval_arith`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Fml.eval_arith), [`MIPRE.SAT.Fml.degreeOf_arith_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Fml.degreeOf_arith_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4991](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4991)
