---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Adapter.pushforward_le
statement: formalized
proof: formalized
---

# The adapter's cost in the question distributions

Average the family of Lemma [The adapter's two maps, and acceptance](lem-lidt-cl-adapter-maps.md) over the seed positions and the scale, uniformly and independently. Then for every seeded question pair $(x,y)$ the average canonical-line mass of its preimage is at most $3m$ times the seeded mass of $(x,y)$.

## Depends on

- [The adapter's two maps, and acceptance](lem-lidt-cl-adapter-maps.md)
- [Seeded CL low individual degree test](def-lidt-cl.md)
- [Canonical-line low individual degree test](def-lidt.md)

## Proof depends on

- [The two complements](../../structure-of-the-proof/part-01/lem-cl-canonical.md)

## Proof

Both distributions are sums over a sample type against an indicator, so the bound is a count of samples. Reordering the average puts it as a weight times a count of *family members*, and that is what the shapes differ in: the image of a point question does not depend on the family member at all, while a line question's pins the seed position at one index and, for a diagonal line, the scale as well.

Four of the nine shapes carry no weight, by the structural remark above. For a pair of points the averaging is neutral and the requirement is $1/(3q^m)\leq C/(9q^m)$. For an axis-parallel line against a point the single contributing sample has weight $1/(6mq^m)$, the family is pinned at one of $m$ indices, and the seeded test puts at least $1/(9q^{m+1})$ on the pair, so $C\geq3/2$ suffices — the factor $q/m$ a fixed seed choice would have cost, paid back exactly by the averaging. For a diagonal line the crude bound “number of contributing samples times the largest of their weights” replaces the geometric series over the admissible $j$, which costs a factor $m$ and nothing in $q$; with the scale pinned as well the constant is $3q/(2(q-1))$, which $3m$ covers for every $q\geq2$.

Two points where the design is forced rather than free. Carrying the direction unrescaled would concentrate the push-forward on a $1/(q-1)$ fraction of the seeded questions describing the same line, and force $C$ to grow with $q$; averaging over one global scale fixes it. And a *singleton* line — direction zero — must be sent to a seed with $\chi=m-1$, not $\chi=0$: the seeded test has $q^{\chi}$ samples for such a question, so only the largest $\chi$ dominates the canonical-line mass, and the wrong choice costs a factor $q^{m-1}$.

## Lean

Formalized as [`MIPRE.LIDT.Adapter.pushforward_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Adapter.pushforward_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 856](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L856)
