---
declaration: lemma
origin: cited
lean: Finset.card_sq_le_card_mul_addEnergy'
statement: formalized
proof: formalized
---

# Cauchy–Schwarz bound

If $G$ is a finite additive group and $A,B$ are subsets of $G$, then

$$
\left( \frac{|\{ (a,a') \in A \times A: a+a' \in B \}|}{|G|^2} \right)^2
\leq \frac{|B|}{|G|}\, E(A).
$$

The left-hand side is the square of the density of a subset of $G \times G$, and the right-hand side involves the density of a subset of $G$.

## Depends on

- [Additive energy](energy-def.md)

## Proof

If $B$ is empty then the claim is trivial (with the Lean convention $0/0$), so without loss of generality $B$ is non-empty. We can rewrite

$$
|\{ (a,a') \in A \times A: a+a' \in B \}| = \sum_{b \in B} r(b)
$$

where $r: G \to \mathbb{N}$ is the counting function

$$
r(b) := |\{ (a,a') \in A \times A: a+a' = b \}|.
$$

From double counting we have

$$
\sum_{b \in G} r(b)^2 = |G|^3 E(A).
$$

The Cauchy–Schwarz inequality then gives

$$
\Bigl( \sum_{b \in B} r(b) \Bigr)^2 \leq |B| \sum_{b \in B} r(b)^2
\leq |B| \sum_{b \in G} r(b)^2 = |B|\, |G|^3 E(A),
$$

and the claim follows on dividing both sides by $|G|^4$.

## Lean

Formalized as [`Finset.card_sq_le_card_mul_addEnergy'`](https://teorth.github.io/pfr/docs/find/#doc/Finset.card_sq_le_card_mul_addEnergy').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 14](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/approx_hom_pfr.tex#L14)
