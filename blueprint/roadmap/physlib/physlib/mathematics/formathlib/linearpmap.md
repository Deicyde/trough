---
declaration: module
origin: cited
lean: LinearPMap.sub_le_zero, LinearPMap.neg_add_le_zero, LinearPMap.le_iff_neg_le_neg, LinearPMap.le_neg_iff_neg_le, LinearPMap.add_sub_le_cancel, LinearPMap.add_sub_le_cancel_left, LinearPMap.add_sub_le_cancel_right, LinearPMap.add_add_sub_le_cancel
statement: formalized
proof: formalized
---

# LinearPMap

The module `Physlib.Mathematics.ForMathlib.LinearPMap`, [Physlib/Mathematics/ForMathlib/LinearPMap.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean): 55 declarations, 6 with a docstring.

## i. Overview

> In this module we collect some basic results about `LinearPMap`s.
>
> Most important is the definition of restricted composition.
> The composition of two partial linear maps `g : F →ₗ.[R] G` and `f : E →ₗ.[R] F` is defined
> only if the range of `f` is contained in the domain of `g` (c.f. `LinearPMap.comp`).
> `g.compRestricted f` (`g ∘ᵣ f`) is defined to be the composition of `g` with the restriction of `f`
> to exactly those `x : f.domain` for which `f x ∈ g.domain`. This allows one to work with the
> composition of partial linear maps while having the domain implicitly accounted for.

## ii. Key results

> - `LinearPMap.sum` : The finite sum of partial linear maps.
> - `LinearPMap.compRestricted` (`∘ᵣ`) : For two partial linear maps
>     `g : F →ₗ[R] G` and `f : E →ₗ[R] F`, the composition of `g` with `f`
>     with natural domain `{x : f.domain | f x ∈ g.domain}`.
> - `LinearPMap.instMonoid` : Partial linear maps `E →ₗ.[R] E` with `compRestricted`
>     for multiplication and the identity map for `1` comprise a monoid.

## iv. References

> * None.

## A. Inequalities

**`LinearPMap.sub_le_zero`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L65).

```lean
lemma sub_le_zero : f - f ≤ 0
```

**`LinearPMap.neg_add_le_zero`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L67).

```lean
lemma neg_add_le_zero : -f + f ≤ 0
```

**`LinearPMap.le_iff_neg_le_neg`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L69).

```lean
lemma le_iff_neg_le_neg : g₁ ≤ g₂ ↔ -g₁ ≤ -g₂
```

**`LinearPMap.le_neg_iff_neg_le`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L72).

```lean
lemma le_neg_iff_neg_le : g₁ ≤ -g₂ ↔ -g₁ ≤ g₂
```

**`LinearPMap.add_sub_le_cancel`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L74).

```lean
lemma add_sub_le_cancel : f₁ + (f₂ - f₁) ≤ f₂
```

**`LinearPMap.add_sub_le_cancel_left`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L77).

```lean
lemma add_sub_le_cancel_left : f₁ + f₂ - f₁ ≤ f₂
```

**`LinearPMap.add_sub_le_cancel_right`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L79).

```lean
lemma add_sub_le_cancel_right : f₁ + f₂ - f₂ ≤ f₁
```

**`LinearPMap.add_add_sub_le_cancel`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L81).

```lean
lemma add_add_sub_le_cancel : f₁ + f₂ + (f₃ - f₂) ≤ f₁ + f₃
```

**`LinearPMap.add_sub_sub_le_cancel`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L84).

```lean
lemma add_sub_sub_le_cancel : f₁ + f₂ - (f₁ - f₃) ≤ f₂ + f₃
```

**`LinearPMap.sub_sub_sub_le_cancel_right`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L87).

```lean
lemma sub_sub_sub_le_cancel_right : f₁ - f₂ - (f₃ - f₂) ≤ f₁ - f₃
```

**`LinearPMap.sub_sub_sub_le_cancel_left`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L91).

```lean
lemma sub_sub_sub_le_cancel_left : f₁ - f₂ - (f₁ - f₃) ≤ f₃ - f₂
```

**`LinearPMap.sub_le_of_le_add`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L94).

```lean
lemma sub_le_of_le_add (h : g ≤ g₁ + g₂) : g - g₂ ≤ g₁
```

**`LinearPMap.sub_add_le_cancel`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L100).

```lean
lemma sub_add_le_cancel : f₁ - f₂ + f₂ ≤ f₁
```

**`LinearPMap.add_le_of_le_sub`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L103).

```lean
lemma add_le_of_le_sub (h : g ≤ g₁ - g₂) : g + g₂ ≤ g₁
```

**`LinearPMap.add_left_le_of_le`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L106).

```lean
lemma add_left_le_of_le (h : g₁ ≤ g₂) : f + g₁ ≤ f + g₂
```

**`LinearPMap.add_right_le_of_le`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L113).

```lean
lemma add_right_le_of_le (h : g₁ ≤ g₂) : g₁ + f ≤ g₂ + f
```

**`LinearPMap.sub_right_le_of_le`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L116).

```lean
lemma sub_right_le_of_le (h : g₁ ≤ g₂) : g₁ - f ≤ g₂ - f
```

**`LinearPMap.sub_left_le_of_le`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L119).

```lean
lemma sub_left_le_of_le (h : g₁ ≤ g₂) : f - g₁ ≤ f - g₂
```

## B. Zero smul

**`LinearPMap.zero_smul_le`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L132).

```lean
lemma zero_smul_le (f : E →ₗ.[𝕜] F) : (0 : 𝕜) • f ≤ 0
```

**`LinearPMap.zero_smul_eq`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L135).

```lean
lemma zero_smul_eq {f : E →ₗ.[𝕜] F} (h : f.domain = ⊤) : (0 : 𝕜) • f = 0
```

## C. Finite sums

**`LinearPMap.sum`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L152).

> A finite sum of partial linear maps.
>
> `sum f` and `∑ a, f a` are equal, but not by definition.
> With `sum f` both `domain` and `toFun` are made explicit.

```lean
def sum : E →ₗ.[R] F
```

**`LinearPMap.sum_domain`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L156).

```lean
lemma sum_domain : (sum f).domain = ⨅ a, (f a).domain
```

**`LinearPMap.sum_domain_le`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L158).

```lean
lemma sum_domain_le (a : α) : (sum f).domain ≤ (f a).domain
```

**`LinearPMap.sum_apply`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L161).

```lean
lemma sum_apply (ψ : (sum f).domain) : sum f ψ = ∑ a, f a ⟨ψ, sum_domain_le f a ψ.2⟩
```

## D. Restricted composition

**`LinearPMap.compRestricted`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L178).

> `g ∘ᵣ f` is the composition of `g` with `f` restricted to a domain consisting of exactly those
> `x : f.domain` for which `f x ∈ g.domain`.

```lean
def compRestricted : E →ₗ.[R] G
```

**`LinearPMap.compRestricted_domain_le`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L190).

```lean
lemma compRestricted_domain_le : (g ∘ᵣ f).domain ≤ f.domain
```

**`LinearPMap.compRestricted_domain`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L192).

```lean
lemma compRestricted_domain : (g ∘ᵣ f).domain = (g.domain.comap f.toFun).map f.domain.subtype
```

**`LinearPMap.mem_compRestricted_domain_iff`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L201).

```lean
lemma mem_compRestricted_domain_iff {x : E} :
    x ∈ (v ∘ᵣ u).domain ↔ ∃ h : x ∈ u.domain, u ⟨x, h⟩ ∈ v.domain
```

**`LinearPMap.mem_compRestricted_domain_iff'`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L205).

```lean
lemma mem_compRestricted_domain_iff' {x : E} :
    x ∈ (v ∘ᵣ u).domain ↔ ∃ y : u.domain, x = y ∧ ∃ y' : v.domain, u y = y'
```

**`LinearPMap.mem_domain_of_mem_compRestricted_domain`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L209).

```lean
lemma mem_domain_of_mem_compRestricted_domain (x : (v ∘ᵣ u).domain) : u ⟨x, x.2.2⟩ ∈ v.domain
```

**`LinearPMap.compRestricted_apply`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L213).

```lean
lemma compRestricted_apply (x : (v ∘ᵣ u).domain) :
    (v ∘ᵣ u) x = v ⟨u ⟨x, x.2.2⟩, mem_domain_of_mem_compRestricted_domain x⟩
```

**`LinearPMap.compRestricted_zero`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L218).

> The zero map is right-absorbing.

```lean
lemma compRestricted_zero : g ∘ᵣ (0 : E →ₗ.[R] F) = 0
```

**`LinearPMap.compRestricted_assoc`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L223).

```lean
lemma compRestricted_assoc {H : Type*} [AddCommGroup H] [Module R H]
    (f₁ : G →ₗ.[R] H) (f₂ : F →ₗ.[R] G) (f₃ : E →ₗ.[R] F) :
    (f₁ ∘ᵣ f₂) ∘ᵣ f₃ = f₁ ∘ᵣ f₂ ∘ᵣ f₃
```

**`LinearPMap.compRestricted_eq_comp`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L232).

> `compRestricted` is the same as `comp` when the range of `u` is contained in `v.domain`.

```lean
lemma compRestricted_eq_comp (h : ∀ x : u.domain, u x ∈ v.domain) :
    v ∘ᵣ u = v.comp u h
```

**`LinearPMap.comp_le_compRestricted`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L240).

> `compRestricted` is maximal amongst compositions of `v` with domain restrictions of `u`.

```lean
lemma comp_le_compRestricted
    {S : Submodule R E} (h : ∀ x : (u.domRestrict S).domain, u ⟨x, x.2.2⟩ ∈ v.domain) :
    v.comp (u.domRestrict S) h ≤ v ∘ᵣ u
```

**`LinearPMap.compRestricted_mono_left`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L245).

```lean
lemma compRestricted_mono_left {g g' : F →ₗ.[R] G} (h : g ≤ g') (f : E →ₗ.[R] F) :
    g ∘ᵣ f ≤ g' ∘ᵣ f
```

**`LinearPMap.compRestricted_mono_right`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L255).

```lean
lemma compRestricted_mono_right (g : F →ₗ.[R] G) {f f' : E →ₗ.[R] F} (h : f ≤ f') :
    g ∘ᵣ f ≤ g ∘ᵣ f'
```

**`LinearPMap.neg_compRestricted`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L265).

```lean
lemma neg_compRestricted : (-g) ∘ᵣ f = -g ∘ᵣ f
```

**`LinearPMap.compRestricted_neg`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L268).

```lean
lemma compRestricted_neg : g ∘ᵣ (-f) = -g ∘ᵣ f
```

**`LinearPMap.add_compRestricted`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L274).

```lean
lemma add_compRestricted : (g₁ + g₂) ∘ᵣ f = g₁ ∘ᵣ f + g₂ ∘ᵣ f
```

**`LinearPMap.sub_compRestricted`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L280).

```lean
lemma sub_compRestricted : (g₁ - g₂) ∘ᵣ f = g₁ ∘ᵣ f - g₂ ∘ᵣ f
```

**`LinearPMap.compRestricted_add_ge`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L283).

```lean
lemma compRestricted_add_ge : g ∘ᵣ f₁ + g ∘ᵣ f₂ ≤ g ∘ᵣ (f₁ + f₂)
```

**`LinearPMap.compRestricted_sub_ge`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L294).

```lean
lemma compRestricted_sub_ge : g ∘ᵣ f₁ - g ∘ᵣ f₂ ≤ g ∘ᵣ (f₁ - f₂)
```

**`LinearPMap.compRestricted_smul`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L298).

```lean
lemma compRestricted_smul {S : Type*} [DivisionRing S]
    [Module S E] [Module S F] [Module S G] [SMulCommClass S S F] [SMulCommClass S S G]
    {c : S} (hc : c ≠ 0) (g : F →ₗ.[S] G) (f : E →ₗ.[S] F) :
    g ∘ᵣ (c • f) = c • (g ∘ᵣ f)
```

**`LinearPMap.smul_compRestricted`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L308).

```lean
lemma smul_compRestricted {M : Type*} [Monoid M] [DistribMulAction M G] [SMulCommClass R M G]
    (c : M) (g : F →ₗ.[R] G) (f : E →ₗ.[R] F) :
    (c • g) ∘ᵣ f = c • (g ∘ᵣ f)
```

## E. Monoid

> Partial linear maps `E →ₗ.[R] E` with `compRestricted` for multiplication and
> the identity map (domain `⊤`) for `1` comprise a monoid.

**`LinearPMap.instMonoid`**, an instance, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L326).

```lean
instance instMonoid : Monoid (E →ₗ.[R] E)
```

**`LinearPMap.mul_def`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L341).

```lean
lemma mul_def (f₁ f₂ : E →ₗ.[R] E) : f₁ * f₂ = f₁ ∘ᵣ f₂
```

**`LinearPMap.one_domain`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L344).

```lean
lemma one_domain : (1 : E →ₗ.[R] E).domain = ⊤
```

**`LinearPMap.one_toFun`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L347).

```lean
lemma one_toFun : (1 : E →ₗ.[R] E).toFun = topEquiv.toLinearMap
```

**`LinearPMap.one_coe`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L350).

```lean
lemma one_coe : (1 : E →ₗ.[R] E).toFun' = ⇑topEquiv.toLinearMap
```

## F. Inverses

**`LinearPMap.toFun_ker_eq_bot_iff`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L361).

> The kernel of `f.toFun` is trivial exactly when the kernel of `f` is.

```lean
lemma toFun_ker_eq_bot_iff {f : E →ₗ.[R] F} : f.toFun.ker = ⊥ ↔ f.ker = ⊥
```

**`LinearPMap.inverse_ker`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L368).

```lean
lemma inverse_ker : f.inverse.toFun.ker = ⊥
```

**`LinearPMap.inverse_inverse`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L373).

```lean
lemma inverse_inverse : f.inverse.inverse = f
```

**`LinearPMap.inverse_compRestricted_eq`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L381).

```lean
lemma inverse_compRestricted_eq : f.inverse ∘ᵣ f = domRestrict 1 f.domain
```

**`LinearPMap.compRestricted_inverse_eq`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean#L386).

```lean
lemma compRestricted_inverse_eq : f ∘ᵣ f.inverse = domRestrict 1 f.inverse.domain
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/LinearPMap.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearPMap.lean)
