---
declaration: module
origin: cited
lean: ProbDistribution.nonempty, ProbDistribution.constant_of_exists_one, ProbDistribution.congr_symm_apply, ProbDistribution.fin_two_eq_coin, ProbDistribution.expect_val_eq_mixable_mix, ProbDistribution.expect_val_constant, ProbDistribution.zero_le_expect_val, ProbDistribution.expect_val_congr_eq_expect_val
statement: formalized
proof: formalized
---

# Distributions on finite sets

The module `QuantumInfo.ClassicalInfo.Distribution`, [QuantumInfo/ClassicalInfo/Distribution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean): 40 declarations, 23 with a docstring, 8 listed as significant.

> We define the type `Distribution α` on a `Fintype α`. By restricting ourselves to distributoins on
> finite types, a lot of notation and casts are greatly simplified.
> This suffices for (most) finite-dimensional quantum theory.

**`ProbDistribution`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L37).

> We define our own (discrete) probability distribution notion here, instead
> of using `PMF` from Mathlib, because that uses ENNReals everywhere to maintain compatibility
> with `MeasureTheory.Measure`.
>
> The probabilities internal to a Distribution are NNReals. This lets us more easily
> write the statement that they sum to 1, since NNReals can be added. (Probabilities,
> on their own, cannot.) But the FunLike instance gives `Prob` out, which carry the
> information that they are all in the range [0,1].

```lean
def ProbDistribution (α : Type u) [Fintype α] : Type u
```

**`ProbDistribution.mk'`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L46).

> Make a distribution, proving only that the values are nonnegative and that the
> sum is 1. The fact that the values are at most 1 is derived as a consequence.

```lean
def mk' (f : α → ℝ) (h₁ : ∀i, 0 ≤ f i) (hN : ∑ i, f i = 1) : ProbDistribution α
```

**`ProbDistribution.instFunLikeProb`**, an instance, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L53).

```lean
instance instFunLikeProb : FunLike (ProbDistribution α) α Prob
```

**`ProbDistribution.normalized`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L60).

```lean
lemma normalized (d : ProbDistribution α) : Finset.sum Finset.univ (fun i ↦ (d i : ℝ)) = 1
```

**`ProbDistribution.prob`**, an abbrev, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L63).

```lean
abbrev prob (d : ProbDistribution α)
```

**`ProbDistribution.fun_eq_val`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L66).

```lean
lemma fun_eq_val (d : ProbDistribution α) : d.val = d
```

**`ProbDistribution.funlike_apply`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L70).

```lean
lemma funlike_apply (d : α → Prob) (h : _) (x : α) :
    DFunLike.coe (self := instFunLikeProb) ⟨d, h⟩ x = d x
```

**`ProbDistribution.ext`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L75).

```lean
lemma ext {p q : ProbDistribution α} (h : ∀ x, p x = q x) : p = q
```

**`ProbDistribution.nonempty`**, a theorem, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L79). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A distribution provides a witness that d is nonempty.

```lean
theorem nonempty (d : ProbDistribution α) : Nonempty α
```

**`ProbDistribution.constant`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L86).

> Make an constant distribution: supported on a single element. This is also called, variously, a
> "One-point distribution", a "Degenerate distribution", a "Deterministic distribution", a
> "Delta function", or a "Point mass distribution".

```lean
def constant (x : α) : ProbDistribution α
```

**`ProbDistribution.constant_def`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L90).

```lean
lemma constant_def (x : α) : (constant x : α → Prob) = fun y ↦ if x = y then 1 else 0
```

**`ProbDistribution.constant_eq`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L94).

```lean
lemma constant_eq (x : α) : constant x y = if x = y then 1 else 0
```

**`ProbDistribution.constant_def'`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L98).

```lean
lemma constant_def' (x y : α) : (constant x : α → Prob) y = if x = y then 1 else 0
```

**`ProbDistribution.constant_of_exists_one`**, a theorem, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L106). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a distribution has an element with probability 1, the distribution has a constant.

```lean
theorem constant_of_exists_one {D : ProbDistribution α} {x : α} (h : D x = 1) :
    D = ProbDistribution.constant x
```

**`ProbDistribution.uniform`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L123).

> Make an uniform distribution.

```lean
def uniform [n : Nonempty α] : ProbDistribution α
```

**`ProbDistribution.uniform_def`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L130).

```lean
lemma uniform_def [Nonempty α] (y : α) : ((uniform y) : ℝ) = 1 / (Finset.univ.card (α := α))
```

**`ProbDistribution.prod`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L134).

> Make a distribution on a product of two Fintypes.

```lean
def prod (d1 : ProbDistribution α) (d2 : ProbDistribution β) : ProbDistribution (Prod α β)
```

**`ProbDistribution.prod_def`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L139).

```lean
lemma prod_def (x : α) (y : β) : prod d1 d2 ⟨x, y⟩ = (d1 x) * (d2 y)
```

**`ProbDistribution.extend_right`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L144).

> Given a distribution on α, extend it to a distribution on `Sum α β` by
> giving it no support on `β`.

```lean
def extend_right (d : ProbDistribution α) : ProbDistribution (α ⊕ β)
```

**`ProbDistribution.extend_left`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L149).

> Given a distribution on α, extend it to a distribution on `Sum β α` by
> giving it no support on `β`.

```lean
def extend_left (d : ProbDistribution α) : ProbDistribution (β ⊕ α)
```

**`ProbDistribution.instMixable`**, an instance, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L154).

> Make a convex mixture of two distributions on the same set.

```lean
instance instMixable : Mixable (α → ℝ) (ProbDistribution α)
```

**`ProbDistribution.relabel`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L161).

> Given a distribution on type α and an equivalence to type β, get the corresponding
> distribution on type β.

```lean
def relabel (d : ProbDistribution α) (σ : β ≃ α) : ProbDistribution β
```

**`ProbDistribution.congr`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L170).

> ProbDistribution on α and β are equivalent for equivalent types α ≃ β.

```lean
def congr (σ : α ≃ β) : ProbDistribution α ≃ ProbDistribution β
```

**`ProbDistribution.congr_apply`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L186).

```lean
lemma congr_apply (σ : α ≃ β) (d : ProbDistribution α) (j : β): (congr σ d) j = d (σ.symm j)
```

**`ProbDistribution.congr_symm_apply`**, a theorem, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L191). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The inverse and congruence operations for distributions commute

```lean
theorem congr_symm_apply (σ : α ≃ β) :
    (ProbDistribution.congr σ).symm = ProbDistribution.congr σ.symm
```

**`ProbDistribution.coin`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L197).

> The distribution on Fin 2 corresponding to a coin with probability p.
> Chance p of 1, 1-p of 0.

```lean
def coin (p : Prob) : ProbDistribution (Fin 2)
```

**`ProbDistribution.coin_val_zero`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L201).

```lean
lemma coin_val_zero (p : Prob) : coin p 0 = p
```

**`ProbDistribution.coin_val_one`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L205).

```lean
lemma coin_val_one (p : Prob) : coin p 1 = 1 - p
```

**`ProbDistribution.fin_two_eq_coin`**, a theorem, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L209). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every distribution on two variable is some coin.

```lean
theorem fin_two_eq_coin (d : ProbDistribution (Fin 2)) : d = coin (d 0)
```

**`ProbDistribution.coin_eq_iff`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L217).

```lean
lemma coin_eq_iff (p : Prob) (f : ProbDistribution (Fin 2)) :
    ProbDistribution.coin p = f ↔ p = f 0
```

**`ProbDistribution.RandVar`**, a structure, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L229).

> A `T`-valued random variable over `α` is a map `var : α → T` along
> with a probability distribution `distr : Distribution α`.

```lean
structure RandVar (α : Type*) [Fintype α] (T : Type*) where
  var : α → T
  distr : ProbDistribution α
```

**`ProbDistribution.instFunctor`**, an instance, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L233).

```lean
instance instFunctor : Functor (RandVar α)
```

**`ProbDistribution.instLawfulFunctor`**, an instance, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L235).

```lean
instance instLawfulFunctor : LawfulFunctor (RandVar α)
```

**`ProbDistribution.expect_val`**, a def, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L247).

> `Distribution.exp_val` is the expectation value of a random variable `X`. Under the hood,
> it is the "convex combination over a finite family" on the type `T`, afforded by
> the `Mixable` instance, with the probability distribution of `X` as weights.

```lean
def expect_val (X : RandVar α T) : T
```

**`ProbDistribution.expect_val_eq_mixable_mix`**, a theorem, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L260). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The expectation value of a random variable over `α = Fin 2` is the same as `Mixable.mix`
> with probabiliy weight `X.distr 0`

```lean
theorem expect_val_eq_mixable_mix (d : ProbDistribution (Fin 2)) (x₁ x₂ : T) :
    expect_val ⟨![x₁, x₂], d⟩ = Mixable.mix (d 0) x₁ x₂
```

**`ProbDistribution.expect_val_constant`**, a theorem, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L278). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The expectation value of a random variable with constant probability distribution
> `constant x` is its value at `x`

```lean
theorem expect_val_constant (x : α) (f : α → T) : expect_val ⟨f, (constant x)⟩ = f x
```

**`ProbDistribution.zero_le_expect_val`**, a theorem, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L284). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The expectation value of a nonnegative real random variable is also nonnegative

```lean
theorem zero_le_expect_val (d : ProbDistribution α) (f : α → ℝ) (hpos : 0 ≤ f) :
    0 ≤ expect_val ⟨f, d⟩
```

**`ProbDistribution.congrRandVar`**, a def, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L293).

> `T`-valued random variables on `α` and `β` are equivalent if `α ≃ β`

```lean
def congrRandVar (σ : α ≃ β) : RandVar α T ≃ RandVar β T
```

**`ProbDistribution.map_congr_eq_congr_map`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L313).

> Given a `T`-valued random variable `X` over `α`, mapping over `T` commutes
> with the equivalence over `α`

```lean
lemma map_congr_eq_congr_map {S : Type _} [Mixable U S] (f : T → S) (σ : α ≃ β) (X : RandVar α T) :
  f <$> congrRandVar σ X = congrRandVar σ (f <$> X)
```

**`ProbDistribution.expect_val_congr_eq_expect_val`**, a theorem, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean#L319). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The expectation value is invariant under equivalence of random variables

```lean
theorem expect_val_congr_eq_expect_val (σ : α ≃ β) (X : RandVar α T) :
    expect_val (congrRandVar σ X) = expect_val X
```

## Depends on

- [Probabilities](prob.md)

## Sources

- [QuantumInfo/ClassicalInfo/Distribution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Distribution.lean)
