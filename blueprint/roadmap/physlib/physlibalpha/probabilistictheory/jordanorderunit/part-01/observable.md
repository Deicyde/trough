---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsJordanOrderUnit.moment, ProbabilisticTheory.IsJordanOrderUnit.moment_zero, ProbabilisticTheory.IsJordanOrderUnit.moment_one, ProbabilisticTheory.IsJordanOrderUnit.variance, ProbabilisticTheory.IsJordanOrderUnit.variance_eq, ProbabilisticTheory.IsJordanOrderUnit.moment_two_nonneg, ProbabilisticTheory.JordanAlgebra.IsJordanProjection, ProbabilisticTheory.JordanAlgebra.JordanOrthogonal
statement: formalized
proof: formalized
---

# Moments, variance and Jordan projections

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Observable`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean): 26 declarations, 18 with a docstring.

> Moments and variance of observables, and Jordan projections as effects and compressions.

## i. Overview

> The `n`-th moment of an observable `a` in a state `ω` is `ω(aⁿ)`, and the variance is `ω(a²) -
> ω(a)²`. A Jordan projection is an observable `p` with `p ∘ p = p`, and two projections are
> orthogonal when `p ∘ q = 0`. A Jordan projection is an effect, and its quadratic representation
> `U_p` compresses onto it.

## ii. Key results

> - `IsJordanOrderUnit.moment`, `IsJordanOrderUnit.variance` : moments and variance.
> - `JordanAlgebra.IsJordanProjection`, `JordanAlgebra.JordanOrthogonal` : Jordan projections and
>   orthogonality.
> - `JordanAlgebra.IsJordanProjection.toEffect` : a projection as an effect.

## iv. References

> * None.

## A. Moments and variance

**`ProbabilisticTheory.IsJordanOrderUnit.moment`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L61).

> The `n`-th moment of the observable `a` in the state `ω`: `moment_n(ω, a) = ω(a^n)`.

```lean
def moment (n : ℕ) (ω : 𝓢[ℝ, E]) (a : E) : ℝ
```

**`ProbabilisticTheory.IsJordanOrderUnit.moment_zero`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L63).

```lean
lemma moment_zero (ω : 𝓢[ℝ, E]) (a : E) : moment 0 ω a = 1
```

**`ProbabilisticTheory.IsJordanOrderUnit.moment_one`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L67).

```lean
lemma moment_one (ω : 𝓢[ℝ, E]) (a : E) : moment 1 ω a = ω a
```

**`ProbabilisticTheory.IsJordanOrderUnit.variance`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L72).

> The variance of the observable `a` in the state `ω`, inherited from the generic covariance
> form of its underlying linear functional.

```lean
def variance (ω : 𝓢[ℝ, E]) (a : E) : ℝ
```

**`ProbabilisticTheory.IsJordanOrderUnit.variance_eq`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L75).

> The variance is expressed directly, unfolding `moment 2` to the Jordan square.

```lean
lemma variance_eq (ω : 𝓢[ℝ, E]) (a : E) : variance ω a = ω (a * a) - (ω a) ^ 2
```

**`ProbabilisticTheory.IsJordanOrderUnit.moment_two_nonneg`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L81).

> The second moment of any observable is nonnegative: it is the state's value on the
> (possible-outcome) Jordan square.

```lean
lemma moment_two_nonneg (ω : 𝓢[ℝ, E]) (a : E) : 0 ≤ moment 2 ω a
```

## B. Jordan projections and orthogonality

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L101).

> A Jordan projection: an element idempotent for the Jordan product, `p ∘ p = p`. The
> Jordan-algebraic analogue of a self-adjoint projection, and (in the canonical C⋆-algebra
> realization) exactly an ordinary projection `p² = p = p⋆`.

```lean
def IsJordanProjection (p : E) : Prop
```

**`ProbabilisticTheory.JordanAlgebra.JordanOrthogonal`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L105).

> Two elements are Jordan-orthogonal when their Jordan product vanishes, `p ∘ q = 0`: the
> Jordan-algebraic analogue of `Effect.Orthogonal`.

```lean
def JordanOrthogonal (p q : E) : Prop
```

**`ProbabilisticTheory.JordanAlgebra.isJordanProjection_zero`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L107).

```lean
lemma isJordanProjection_zero : IsJordanProjection (0 : E)
```

**`ProbabilisticTheory.JordanAlgebra.isJordanProjection_one`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L110).

```lean
lemma isJordanProjection_one : IsJordanProjection (1 : E)
```

**`ProbabilisticTheory.JordanAlgebra.jordanOrthogonal_comm`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L112).

```lean
lemma jordanOrthogonal_comm {p q : E} (h : JordanOrthogonal p q) : JordanOrthogonal q p
```

**`ProbabilisticTheory.JordanAlgebra.jordanOrthogonal_zero_left`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L116).

```lean
lemma jordanOrthogonal_zero_left (p : E) : JordanOrthogonal 0 p
```

**`ProbabilisticTheory.JordanAlgebra.jordanOrthogonal_zero_right`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L119).

```lean
lemma jordanOrthogonal_zero_right (p : E) : JordanOrthogonal p 0
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.nonneg`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L130).

> A Jordan projection is automatically a possible outcome (`0 ≤ p`), since it equals its own
> Jordan square.

```lean
lemma IsJordanProjection.nonneg {p : E} (hp : IsJordanProjection p) : 0 ≤ p
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.add_of_jordanOrthogonal`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L136).

> The sum of two orthogonal Jordan projections is again a Jordan projection: the abstract,
> operator-free analogue of "two orthogonal projections add to a projection", the algebraic content
> behind an event-logic (sharp-effect) sum.

```lean
lemma IsJordanProjection.add_of_jordanOrthogonal {p q : E} (hp : IsJordanProjection p)
    (hq : IsJordanProjection q) (horth : JordanOrthogonal p q) :
    IsJordanProjection (p + q)
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.complement`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L146).

> The complement `1 - p` of a Jordan projection is again a Jordan projection: the Jordan-algebra
> analogue of `Effect.complement`.

```lean
lemma IsJordanProjection.complement {p : E} (hp : IsJordanProjection p) :
    IsJordanProjection (1 - p)
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.jordanOrthogonal_complement`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L153).

> A Jordan projection is orthogonal to its own complement: `p ∘ (1 - p) = 0`.

```lean
lemma IsJordanProjection.jordanOrthogonal_complement {p : E} (hp : IsJordanProjection p) :
    JordanOrthogonal p (1 - p)
```

## C. Projections as effects

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.le_one`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L164).

> A Jordan projection is bounded above by the order unit. Its complement is another projection,
> hence a nonnegative square, and `0 ≤ 1 - p` is exactly `p ≤ 1`.

```lean
lemma IsJordanProjection.le_one {p : E} (hp : IsJordanProjection p) : p ≤ 1
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.toEffect`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L168).

> A Jordan projection, bundled as an effect.

```lean
def IsJordanProjection.toEffect {p : E} (hp : IsJordanProjection p) : Effect E
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.coe_toEffect`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L172).

```lean
lemma IsJordanProjection.coe_toEffect {p : E} (hp : IsJordanProjection p) :
    (hp.toEffect : E) = p
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.toEffect_complement`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L176).

> Bundling a projection's algebraic complement agrees with taking its effect complement.

```lean
lemma IsJordanProjection.toEffect_complement {p : E} (hp : IsJordanProjection p) :
    hp.complement.toEffect = Effect.complement hp.toEffect
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.effectOrthogonal_of_jordanOrthogonal`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L182).

> Jordan-orthogonal projections have a defined partial sum in the effect algebra. This is the
> forward direction that follows from square positivity alone; the converse needs the stronger JB
> order theory.

```lean
lemma IsJordanProjection.effectOrthogonal_of_jordanOrthogonal {p q : E}
    (hp : IsJordanProjection p) (hq : IsJordanProjection q) (hpq : JordanOrthogonal p q) :
    Effect.Orthogonal hp.toEffect hq.toEffect
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.addOfOrthogonal_toEffect`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L189).

> The effect-algebra partial sum of Jordan-orthogonal projections is their algebraic projection
> sum.

```lean
lemma IsJordanProjection.addOfOrthogonal_toEffect {p q : E}
    (hp : IsJordanProjection p) (hq : IsJordanProjection q) (hpq : JordanOrthogonal p q) :
    Effect.addOfOrthogonal hp.toEffect hq.toEffect
      (hp.effectOrthogonal_of_jordanOrthogonal hq hpq) =
        (hp.add_of_jordanOrthogonal hq hpq).toEffect
```

## D. Compression: `U_p` for an idempotent `p`

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_self`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L207).

> **Compression onto an event.** For a Jordan projection `p`, `U_p(p) = p`: compressing `p`
> itself onto the event `p` changes nothing. The Jordan-algebraic seed of "the outcome that already
> happened is unaffected by conditioning on it having happened".

```lean
lemma IsJordanProjection.quadRep_self {p : E} (hp : IsJordanProjection p) : U p p = p
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_jordanOrthogonal`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L214).

> `U_p q = 0` for projections `q` orthogonal to `p`.

```lean
lemma IsJordanProjection.quadRep_jordanOrthogonal {p q : E} (hp : IsJordanProjection p)
    (horth : JordanOrthogonal p q) : U p q = 0
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.quadRep_one`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean#L224).

> **Compression of the unit recovers the event itself.** For a Jordan projection `p`,
> `U_p(1) = p`: this is `quadRep_apply_one` specialized using `p² = p`.

```lean
lemma IsJordanProjection.quadRep_one {p : E} (hp : IsJordanProjection p) : U p (1 : E) = p
```

## Depends on

- [Complementary effects](../../../../physlib/probabilistictheory/effect/complement.md)
- [Statistics of a linear functional on a bilinear algebra](../../algebra/statistics.md)
- [Channels](../../channel/basic.md)
- [Orthogonal effects](../../effect/basic.md)
- [Jordan order-unit spaces](basic.md)
- [Powers, multiplication operators and the quadratic representation](operator.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Observable.lean)
