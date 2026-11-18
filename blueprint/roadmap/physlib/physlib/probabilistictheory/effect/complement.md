---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.complement, ProbabilisticTheory.Effect.coe_complement, ProbabilisticTheory.Effect.complement_complement, ProbabilisticTheory.Effect.complement_antitone, ProbabilisticTheory.Effect.complement_zero, ProbabilisticTheory.Effect.complement_one, ProbabilisticTheory.Effect.complement_mix
statement: formalized
proof: formalized
---

# Complementary effects

The module `Physlib.ProbabilisticTheory.Effect.Complement`, [Physlib/ProbabilisticTheory/Effect/Complement.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean): 7 declarations, 3 with a docstring.

> The complement `1 - e` of an effect, its antitonicity and compatibility with mixtures.

## i. Overview

> The complement of an effect `e` is the yes/no test that fires exactly when `e` doesn't: `1 - e`.
> Physically, a state's probability of "no" is always `1` minus its probability of "yes".

## ii. Key results

> - `Effect.complement` : the complementary effect `1 - e`.
> - `Effect.complement_antitone` : the complement reverses order.
> - `Effect.complement_mix` : the complement of a mixture is the mixture of the complements.

## iv. References

> * None.

## A. The complement

**`ProbabilisticTheory.Effect.complement`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean#L53).

> The complementary effect.

```lean
def complement (e : Effect E) : Effect E
```

**`ProbabilisticTheory.Effect.coe_complement`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean#L57).

```lean
lemma coe_complement (e : Effect E) : ((complement e : Effect E) : E) = 1 - e
```

**`ProbabilisticTheory.Effect.complement_complement`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean#L60).

```lean
lemma complement_complement (e : Effect E) : complement (complement e) = e
```

## B. Monotonicity of the complement

**`ProbabilisticTheory.Effect.complement_antitone`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean#L70).

> The complement reverses order: a more certain test's complement is a less certain one.

```lean
lemma complement_antitone : Antitone (complement (E := E))
```

**`ProbabilisticTheory.Effect.complement_zero`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean#L74).

```lean
lemma complement_zero : complement (0 : Effect E) = 1
```

**`ProbabilisticTheory.Effect.complement_one`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean#L77).

```lean
lemma complement_one : complement (1 : Effect E) = 0
```

## C. The complement and mixtures

**`ProbabilisticTheory.Effect.complement_mix`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean#L86).

> Mixing commutes with taking the complement.

```lean
lemma complement_mix (e f : Effect E) (t : unitInterval) :
    complement (mix e f t) = mix (complement e) (complement f) t
```

## Depends on

- [Convexity and mixtures of effects](convex.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Complement.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Complement.lean)
