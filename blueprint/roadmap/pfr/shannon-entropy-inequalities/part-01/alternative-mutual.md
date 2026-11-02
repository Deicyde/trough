---
declaration: lemma
origin: cited
lean: ProbabilityTheory.mutualInfo_comm, ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy
statement: formalized
proof: formalized
---

# Alternative formulae for mutual information

With notation as above, we have

$$
\mathbb{I}[X : Y] = \mathbb{I}[Y:X]
$$

$$
\mathbb{I}[X : Y] = \mathbb{H}[X] - \mathbb{H}[X|Y]
$$

$$
\mathbb{I}[X : Y] = \mathbb{H}[Y] - \mathbb{H}[Y|X]
$$

## Depends on

- [Mutual information](information-def.md)

## Proof depends on

- [Commutativity and associativity of joint entropy](entropy-comm.md)
- [Chain rule](chain-rule.md)

## Proof

Immediate from Lemmas [Commutativity and associativity of joint entropy](entropy-comm.md), [Chain rule](chain-rule.md).

## Lean

Formalized as [`ProbabilityTheory.mutualInfo_comm`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutualInfo_comm), [`ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 168](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L168)
