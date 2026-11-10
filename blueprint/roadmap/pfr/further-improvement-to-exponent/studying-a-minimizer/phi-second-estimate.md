---
declaration: lemma
origin: cited
lean: I_two_le
statement: formalized
proof: formalized
---

# phi-second-estimate

$I_2\le 2\eta d[X_1;X_2] + \frac{\eta}{1-\eta}(2\eta d[X_1;X_2]-I_1)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [phi-min-def](phi-min-def.md)
- [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md)
- [I1-I2-diff](i1-i2-diff.md)

## Proof

First of all, by $\phi[X_1;X_2]\le \phi[X_1+\tilde X_1;X_2+\tilde X_2]$, $\phi[X_1;X_2]\le \phi[X_1|X_1+\tilde X_1;X_2|X_2+\tilde X_2]$, and the fibring identity obtained by applying [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md) on $(X_1,X_2,\tilde X_1,\tilde X_2)$, we have $I_2\le \eta (d[X_1;X_1]+d[X_2;X_2])$. Then apply [Lemma I1-I2-diff](i1-i2-diff.md) to get $I_2\le 2\eta d[X_1;X_2] +\eta(I_2-I_1)$, and rearrange.

## Lean

Formalized as [`I_two_le`](https://teorth.github.io/pfr/docs/find/#doc/I_two_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 249](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L249)
