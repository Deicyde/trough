---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.complement, ProbabilisticTheory.Effect.coe_complement, ProbabilisticTheory.Effect.complement_complement, ProbabilisticTheory.Effect.complement_antitone, ProbabilisticTheory.Effect.complement_zero, ProbabilisticTheory.Effect.complement_one, ProbabilisticTheory.Effect.complement_mix
statement: formalized
proof: formalized
---

# Complementary effects (Physlib)

The module `Physlib.ProbabilisticTheory.Effect.Complement`, [Physlib/ProbabilisticTheory/Effect/Complement.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean): 7 declarations, 3 with a docstring.

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

**`ProbabilisticTheory.Effect.complement`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean#L51).

> The complementary effect.

```lean
def complement (e : P.Effect) : P.Effect
```

**`ProbabilisticTheory.Effect.coe_complement`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean#L55).

```lean
lemma coe_complement (e : P.Effect) : ((complement e : P.Effect) : P.Observables) = 1 - e
```

**`ProbabilisticTheory.Effect.complement_complement`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean#L58).

```lean
lemma complement_complement (e : P.Effect) : complement (complement e) = e
```

## B. Monotonicity of the complement

**`ProbabilisticTheory.Effect.complement_antitone`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean#L68).

> The complement reverses order: a more certain test's complement is a less certain one.

```lean
lemma complement_antitone : Antitone (complement (P := P))
```

**`ProbabilisticTheory.Effect.complement_zero`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean#L72).

```lean
lemma complement_zero : complement (0 : P.Effect) = 1
```

**`ProbabilisticTheory.Effect.complement_one`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean#L75).

```lean
lemma complement_one : complement (1 : P.Effect) = 0
```

## C. The complement and mixtures

**`ProbabilisticTheory.Effect.complement_mix`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean#L84).

> Mixing commutes with taking the complement.

```lean
lemma complement_mix (e f : P.Effect) (t : unitInterval) :
    complement (mix e f t) = mix (complement e) (complement f) t
```

## Depends on

- [Convexity and mixtures of effects (Physlib)](convex.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Complement.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Complement.lean)
