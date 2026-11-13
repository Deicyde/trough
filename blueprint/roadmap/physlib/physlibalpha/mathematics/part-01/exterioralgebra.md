---
declaration: module
origin: cited
lean: ExteriorAlgebra.derivationGen, ExteriorAlgebra.derivationGen_fst, ExteriorAlgebra.derivationGen_snd, ExteriorAlgebra.derivationGen_mul_self, ExteriorAlgebra.derivationHom, ExteriorAlgebra.derivationHom_ι, ExteriorAlgebra.derivationHom_fst, ExteriorAlgebra.derivationOfLinear
statement: formalized
proof: formalized
---

# Derivations and representations on the exterior algebra

The module `PhyslibAlpha.Mathematics.ExteriorAlgebra`, [PhyslibAlpha/Mathematics/ExteriorAlgebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean): 24 declarations, 12 with a docstring.

## i. Overview

> Mathlib's `ExteriorAlgebra` carries the universal property `ExteriorAlgebra.lift` and the
> functorial map `ExteriorAlgebra.map`, but neither the derivation extending a linear
> endomorphism of the generators nor the representation extending a representation on them.
> This file provides both, as the exterior counterparts of the symmetric-algebra
> constructions in `PhyslibAlpha.Mathematics.SymmetricAlgebra`.
>
> A linear endomorphism `d` of `M` extends uniquely to an *even* derivation of the exterior
> algebra — the Leibniz rule with no Koszul signs — because the generator map
> `ι x ↦ (ι x, ι (d x))` into the trivial square-zero extension squares to zero: degree-one
> elements of an exterior algebra anticommute. A representation of a monoid `G` on `M`
> extends to one on the exterior algebra by functoriality of `ExteriorAlgebra.map`, and every
> element of `G` then acts by an algebra homomorphism.

## ii. Key results

> - `ExteriorAlgebra.derivationOfLinear` : the even derivation extending a linear
>   endomorphism of the generators.
> - `ExteriorAlgebra.derivationOfLinear_mul` : the Leibniz rule.
> - `ExteriorAlgebra.derivationOfLinear_comm_apply` : derivations extending commuting
>   endomorphisms commute.
> - `ExteriorAlgebra.algHom_derivationOfLinear` : an algebra map determined by an
>   intertwining linear map carries one derivation to the other.
> - `Representation.exteriorAlgebra` : the representation extending one on the generators.
> - `Representation.exteriorAlgebra_apply_mul` : each element acts multiplicatively.
> - `ExteriorAlgebra.exteriorAlgebra_derivationOfLinear` : covariance of the derivation
>   under the representation.
> - `ExteriorAlgebra.mapEquiv` : transport of the algebra along a linear equivalence of the
>   generators.
> - `ExteriorAlgebra.algHom_exteriorAlgebra` : an algebra map determined by an intertwining
>   linear map carries one representation to the other.

## iv. References

> * None.

## A. The derivation extending a linear endomorphism

**`ExteriorAlgebra.derivationGen`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L76).

> The generator map of the derivation extending `d`, into the trivial square-zero
> extension of the exterior algebra: `ι x ↦ (ι x, ι (d x))`.

```lean
noncomputable def derivationGen :
    M →ₗ[R] TrivSqZeroExt (ExteriorAlgebra R M) (ExteriorAlgebra R M)
```

**`ExteriorAlgebra.derivationGen_fst`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L83).

```lean
lemma derivationGen_fst (x : M) : (derivationGen d x).fst = ι R x
```

**`ExteriorAlgebra.derivationGen_snd`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L86).

```lean
lemma derivationGen_snd (x : M) : (derivationGen d x).snd = ι R (d x)
```

**`ExteriorAlgebra.derivationGen_mul_self`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L90).

> The generator map squares to zero: degree-one elements of the exterior algebra
> anticommute, which is exactly the square-zero condition on the pair.

```lean
lemma derivationGen_mul_self (x : M) : derivationGen d x * derivationGen d x = 0
```

**`ExteriorAlgebra.derivationHom`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L99).

> The lift of the derivation extending `d` to the trivial square-zero extension of the
> exterior algebra: the algebra homomorphism `x ↦ (x, derivationOfLinear d x)`.

```lean
noncomputable def derivationHom :
    ExteriorAlgebra R M →ₐ[R]
      TrivSqZeroExt (ExteriorAlgebra R M) (ExteriorAlgebra R M)
```

**`ExteriorAlgebra.derivationHom_ι`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L105).

```lean
lemma derivationHom_ι (x : M) : derivationHom d (ι R x) = derivationGen d x
```

**`ExteriorAlgebra.derivationHom_fst`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L110).

> The first component of the square-zero lift is the identity.

```lean
lemma derivationHom_fst (x : ExteriorAlgebra R M) : (derivationHom d x).fst = x
```

**`ExteriorAlgebra.derivationOfLinear`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L122).

> The even derivation of the exterior algebra extending a linear endomorphism `d` of
> `M`: the map obeying the Leibniz rule, with no Koszul signs, whose value on a generator
> `ι x` is `ι (d x)`.

```lean
noncomputable def derivationOfLinear : ExteriorAlgebra R M →ₗ[R] ExteriorAlgebra R M
```

**`ExteriorAlgebra.derivationOfLinear_ι`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L128).

```lean
lemma derivationOfLinear_ι (x : M) : derivationOfLinear d (ι R x) = ι R (d x)
```

**`ExteriorAlgebra.derivationOfLinear_one`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L133).

```lean
lemma derivationOfLinear_one : derivationOfLinear d (1 : ExteriorAlgebra R M) = 0
```

**`ExteriorAlgebra.derivationOfLinear_algebraMap`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L137).

```lean
lemma derivationOfLinear_algebraMap (r : R) :
    derivationOfLinear d (algebraMap R (ExteriorAlgebra R M) r) = 0
```

**`ExteriorAlgebra.derivationOfLinear_mul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L143).

> The Leibniz rule for the derivation extending `d`, with no Koszul signs: the derivation
> is even even though the generators are odd.

```lean
lemma derivationOfLinear_mul (x y : ExteriorAlgebra R M) :
    derivationOfLinear d (x * y)
      = derivationOfLinear d x * y + x * derivationOfLinear d y
```

**`ExteriorAlgebra.derivationOfLinear_comm_apply`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L154).

> Derivations extending commuting endomorphisms commute.

```lean
lemma derivationOfLinear_comm_apply {d₁ d₂ : M →ₗ[R] M} (h : d₁ ∘ₗ d₂ = d₂ ∘ₗ d₁)
    (x : ExteriorAlgebra R M) :
    derivationOfLinear d₁ (derivationOfLinear d₂ x)
      = derivationOfLinear d₂ (derivationOfLinear d₁ x)
```

**`ExteriorAlgebra.algHom_derivationOfLinear`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L172).

> An algebra map carries one derivation to the other when the linear map it is
> determined by on the generators intertwines the two endomorphisms. The hypotheses are
> stated pointwise so that the lemma can be applied without rewriting inside a large
> algebra.

```lean
lemma algHom_derivationOfLinear {N : Type*} [AddCommGroup N] [Module R N]
    (F : ExteriorAlgebra R M →ₐ[R] ExteriorAlgebra R N) {f : M →ₗ[R] N}
    (hF : ∀ x, F (ι R x) = ι R (f x)) {d : M →ₗ[R] M} {d' : N →ₗ[R] N}
    (h : ∀ x, f (d x) = d' (f x)) (y : ExteriorAlgebra R M) :
    F (derivationOfLinear d y) = derivationOfLinear d' (F y)
```

## B. The representation extending a representation on the generators

**`Representation.exteriorAlgebra`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L202).

> The representation on the exterior algebra extending a representation on the
> generators, by functoriality of `ExteriorAlgebra.map`.

```lean
noncomputable def exteriorAlgebra (ρ : Representation R G M) :
    Representation R G (ExteriorAlgebra R M)
```

**`Representation.exteriorAlgebra_apply`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L215).

```lean
lemma exteriorAlgebra_apply (ρ : Representation R G M) (g : G)
    (x : ExteriorAlgebra R M) :
    ρ.exteriorAlgebra g x = ExteriorAlgebra.map (ρ g) x
```

**`Representation.exteriorAlgebra_ι`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L220).

```lean
lemma exteriorAlgebra_ι (ρ : Representation R G M) (g : G) (x : M) :
    ρ.exteriorAlgebra g (ExteriorAlgebra.ι R x) = ExteriorAlgebra.ι R (ρ g x)
```

**`Representation.exteriorAlgebra_apply_one`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L225).

```lean
lemma exteriorAlgebra_apply_one (ρ : Representation R G M) (g : G) :
    ρ.exteriorAlgebra g (1 : ExteriorAlgebra R M) = 1
```

**`Representation.exteriorAlgebra_apply_mul`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L229).

```lean
lemma exteriorAlgebra_apply_mul (ρ : Representation R G M) (g : G)
    (x y : ExteriorAlgebra R M) :
    ρ.exteriorAlgebra g (x * y) = ρ.exteriorAlgebra g x * ρ.exteriorAlgebra g y
```

**`Representation.exteriorAlgebra_algebraMap`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L234).

```lean
lemma exteriorAlgebra_algebraMap (ρ : Representation R G M) (g : G) (r : R) :
    ρ.exteriorAlgebra g (algebraMap R (ExteriorAlgebra R M) r)
      = algebraMap R (ExteriorAlgebra R M) r
```

**`ExteriorAlgebra.exteriorAlgebra_derivationOfLinear`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L251).

> Covariance of the derivation under the representation. If the representation
> carries each endomorphism of a family into a combination of the others on the generators,
> then it carries the derivation extending one into the same combination of the derivations
> extending the others on the whole exterior algebra. This is the shape the statement that
> the total derivative is a Lorentz vector takes; it is proved by induction rather than by
> algebra-map extensionality, a derivation not being an algebra map.

```lean
lemma exteriorAlgebra_derivationOfLinear {G κ : Type*} [Monoid G] [Fintype κ]
    (ρ : Representation R G M) (g : G) (d : κ → M →ₗ[R] M) (μ : κ) (c : κ → R)
    (h : ∀ x, ρ g (d μ x) = ∑ a, c a • d a (ρ g x)) (y : ExteriorAlgebra R M) :
    ρ.exteriorAlgebra g (derivationOfLinear (d μ) y)
      = ∑ a, c a • derivationOfLinear (d a) (ρ.exteriorAlgebra g y)
```

**`ExteriorAlgebra.algHom_exteriorAlgebra`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L281).

> An algebra map carries one representation to the other when the linear map it is
> determined by on the generators intertwines the two representations on them. Unlike the
> derivation statement this is pure extensionality of algebra maps, each group element
> acting by one; the hypotheses are stated pointwise so that the lemma can be applied
> without rewriting inside a large algebra.

```lean
lemma algHom_exteriorAlgebra {N G : Type*} [AddCommGroup N] [Module R N] [Monoid G]
    (F : ExteriorAlgebra R M →ₐ[R] ExteriorAlgebra R N) {f : M →ₗ[R] N}
    (hF : ∀ x, F (ι R x) = ι R (f x))
    {ρ : Representation R G M} {σ : Representation R G N} (g : G)
    (h : ∀ x, f (ρ g x) = σ g (f x)) (y : ExteriorAlgebra R M) :
    F (ρ.exteriorAlgebra g y) = σ.exteriorAlgebra g (F y)
```

## C. Transport along a linear equivalence

> Mathlib's `ExteriorAlgebra.congr` goes through `CliffordAlgebra.equivOfIsometry`, whose
> quadratic-form layer the elaborator cannot see through cheaply once the underlying module is
> a large direct sum. The version below is built from `ExteriorAlgebra.map` instead.

**`ExteriorAlgebra.mapEquiv`**, a def, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L311).

> Transport of an exterior algebra along a linear equivalence, built from
> `ExteriorAlgebra.map` so that no `CliffordAlgebra` isometry has to be unfolded.

```lean
noncomputable def mapEquiv {R M N : Type*} [CommRing R] [AddCommGroup M]
    [Module R M] [AddCommGroup N] [Module R N] (e : M ≃ₗ[R] N) :
    ExteriorAlgebra R M ≃ₐ[R] ExteriorAlgebra R N
```

**`ExteriorAlgebra.mapEquiv_apply_ι`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean#L324).

```lean
lemma mapEquiv_apply_ι {R M N : Type*} [CommRing R] [AddCommGroup M]
    [Module R M] [AddCommGroup N] [Module R N] (e : M ≃ₗ[R] N) (x : M) :
    mapEquiv e (ExteriorAlgebra.ι R x) = ExteriorAlgebra.ι R (e x)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ExteriorAlgebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ExteriorAlgebra.lean)
