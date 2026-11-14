---
declaration: lemma
origin: cited
lean: MIPRE.SeededGame.oracleStrategy, MIPRE.SeededGame.isPCC_oracleStrategy, MIPRE.SeededGame.oracleStrategy_value_eq_one
statement: formalized
proof: formalized
---

# Completeness of oracularization, at the level of games

Let $S = (L^\textsc{A}, L^\textsc{B}, D)$ be a seeded game and let $T$ be a PCC synchronous strategy for the doubled game of $S$, whose questions are $(\mathsf{false}, x)$ for Alice and $(\mathsf{true}, y)$ for Bob. Define a synchronous strategy $\Sigma^\textsc{Orac}(T)$ for the oracularization of $S$, on the same Hilbert space, by

$$
N^{(\textsc{O},\, z)}_{(a,b)} = M^{(\mathsf{false},\, L^\textsc{A}(z))}_a \cdot
M^{(\mathsf{true},\, L^\textsc{B}(z))}_b, \qquad
N^{(\textsc{A},\, x)}_{a} = M^{(\mathsf{false},\, x)}_a, \qquad
N^{(\textsc{B},\, y)}_{b} = M^{(\mathsf{true},\, y)}_b,
$$

and $N^{(v,\, x)}_u = 0$ when the shape of $u$ does not match the role $v$. Then $\Sigma^\textsc{Orac}(T)$ is a synchronous strategy, it is PCC, and if $T$ has value $1$ then so does $\Sigma^\textsc{Orac}(T)$. Both players measure with this one family of operators (Remark [Identical measurement operators](../README.md)).

## Depends on

- [The oracularized game](def-oracular-game.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Synchronous strategy](../../foundations/part-01/def-sync-strategy.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)

## Proof depends on

- [A perfect strategy rejects nothing on the support](../../foundations/part-01/lem-perfect-rejects-nothing.md)

## Proof

That the oracle's operators are projections is where PCC is used: the seed $z$ always lands on a question pair of positive weight, so $M^{(\mathsf{false}, L^\textsc{A}(z))}_a$ and $M^{(\mathsf{true}, L^\textsc{B}(z))}_b$ commute, and a product of two commuting projections is a projection. Their sum over $(a,b)$ is the product of the two sums, hence the identity. The family is PCC because the four operators $M^{(\mathsf{false}, L^\textsc{A}(z))}_a, M^{(\mathsf{true}, L^\textsc{B}(z))}_b$ at one seed commute pairwise — two at one question because distinct outcomes of a projective measurement are orthogonal, one of each by the hypothesis — so every product of them commutes with every other.

For value $1$ it suffices, by Lemma [A perfect strategy rejects nothing on the support](../../foundations/part-01/lem-perfect-rejects-nothing.md) read in the converse direction, that every rejected outcome pair at a question pair of positive weight has probability zero, and in fact each of the decider's checks that can fail makes one of the two operators, or their product, vanish. A shape mismatch gives the zero operator by definition. A pair the input predicate rejects gives the zero operator as well: its probability is zero by Lemma [A perfect strategy rejects nothing on the support](../../foundations/part-01/lem-perfect-rejects-nothing.md), and the normalized trace on matrices is faithful, so a self-adjoint idempotent of vanishing trace is $0$. Check 2(a) is orthogonality of distinct outcomes at a repeated question, which is available because two questions of positive weight with equal roles are equal. Check 2(b) is orthogonality again, after the oracle's other factor has been commuted out of the way.

## Lean

Formalized as [`MIPRE.SeededGame.oracleStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oracleStrategy), [`MIPRE.SeededGame.isPCC_oracleStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.isPCC_oracleStrategy), [`MIPRE.SeededGame.oracleStrategy_value_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oracleStrategy_value_eq_one).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4212](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4212)
