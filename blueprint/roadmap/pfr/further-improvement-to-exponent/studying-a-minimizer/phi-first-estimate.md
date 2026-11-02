---
declaration: lemma
origin: cited
lean: I_one_le
statement: formalized
proof: formalized
---

# phi-first-estimate

$I_1\le 2\eta d[X_1;X_2]$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [phi-min-def](phi-min-def.md)
- [Fibring identity for first estimate](../../entropy-version-of-pfr/first-estimate/first-fibre.md)

## Proof

Similar to [First estimate](../../entropy-version-of-pfr/first-estimate/first-estimate.md): get upper bounds for $d[X_1;X_2]$ by $\phi[X_1;X_2]\le \phi[X_1+X_2;\tilde X_1+\tilde X_2]$ and $\phi[X_1;X_2]\le \phi[X_1|X_1+X_2;\tilde X_2|\tilde X_1+\tilde X_2]$, and then apply [Fibring identity for first estimate](../../entropy-version-of-pfr/first-estimate/first-fibre.md) to get an upper bound for $I_1$.

## Lean

Formalized as [`I_one_le`](https://teorth.github.io/pfr/docs/find/#doc/I_one_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 232](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L232)
