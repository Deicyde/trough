---
declaration: section
origin: cited
lean: Stacks.Chow.gysinHomomorphismOfInvertible, Stacks.Chow.gysinHomomorphismOfInvertible_of_not_le, Stacks.Chow.gysinHomomorphismOfInvertible_of_le, Stacks.Chow.gysinHomomorphismOfInvertible_finsum, Stacks.Chow.effectiveCartierIntersectionOfInvertible, Stacks.Chow.VirtualNormalTriple, Stacks.Chow.VirtualNormalTriple.normalIsoOfIsEffectiveCartier, Stacks.Chow.virtualNormalGysinOfIdeal_zeroScheme
statement: formalized
proof: formalized
---

# 42.29 Gysin homomorphisms

Section 42.29 of the Stacks Project, [Tag 02T7](https://stacks.math.columbia.edu/tag/02T7). 8 tags here are carried by 39 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02T8, a definition

[Tag 02T8](https://stacks.math.columbia.edu/tag/02T8) in the Stacks Project.

**`Stacks.Chow.gysinHomomorphismOfInvertible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernComponent/ClassRule.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernComponent/ClassRule.lean#L132). The attribute's comment: “Gysin homomorphism”.

> The Gysin homomorphism of the zero scheme of a global section `s` of an invertible module:
> `Stacks.Chow.gysinHomomorphism` at the first Chern class component rule of `L`.

```lean
abbrev gysinHomomorphismOfInvertible : CycleGroup C p (k + 1) →+
    chowGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_of_not_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernComponent/ClassRule.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernComponent/ClassRule.lean#L146). The attribute's comment: “integral component not contained in the zero scheme”.

> The Gysin image of an integral closed subscheme not contained in the zero scheme is the class
> of its scheme-theoretic intersection with that zero scheme.

```lean
theorem gysinHomomorphismOfInvertible_of_not_le (W : X.IdealSheafData)
    (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (h : ¬ Stacks.Divisors.zeroScheme X L s ≤ W) :
    gysinHomomorphismOfInvertible C p k L s
        (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
      QuotientAddGroup.mk
        (cycleAssociatedToClosedSubscheme C
          ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
          ((W.comap (Stacks.Divisors.zeroScheme X L s).subschemeι).subschemeι) k)
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean#L151). The attribute's comment: “integral component contained in the zero scheme”.

> The Gysin image of an integral closed subscheme contained in the zero scheme of `s` is the
> proper Chow pushforward into that zero scheme of the first Chern class of `L|_W`.
>
> The instance of Stacks 02S2 that `Stacks.Chow.properChowPushforward` requires is discharged, the
> inclusion of `W` into the zero scheme being a closed immersion.

```lean
theorem gysinHomomorphismOfInvertible_of_le (W : X.IdealSheafData)
    (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (h : Stacks.Divisors.zeroScheme X L s ≤ W) :
    gysinHomomorphismOfInvertible C p k L s
        (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
      properChowPushforward C (W.subschemeι ≫ p)
        ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
        (Scheme.IdealSheafData.inclusion h) (by simp) k
        (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
          (Scheme.IdealSheafData.inclusion h) C (W.subschemeι ≫ p)
          ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (by simp) k)
        (firstChernComponentClass C p k L W hW hDim)
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean#L168). The attribute's comment: “locally finite component formula”.

> The locally finite component formula for the Gysin map of an invertible module.

```lean
theorem gysinHomomorphismOfInvertible_finsum {J : Type u} (W : J → X.IdealSheafData)
    (hW : ∀ j, IsIntegral (W j).subscheme)
    (hDim : ∀ j, schemeDeltaDimension C ((W j).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (hLocal : LocallyFinite fun j ↦ ((W j).support : Set X)) (n : J → ℤ)
    (α : CycleGroup C p (k + 1))
    (hα : ∀ x : X, α.1 x = ∑ᶠ j : J, n j *
      (cycleAssociatedToClosedSubscheme C p (W j).subschemeι (k + 1)).1 x) :
    ∃ β : CycleGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k,
      gysinHomomorphismOfInvertible C p k L s α = QuotientAddGroup.mk β ∧
      ∀ x : (Stacks.Divisors.zeroScheme X L s).subscheme,
        β.1 x = ∑ᶠ j : J, n j *
          (gysinComponentCycle C p k L s (firstChernComponentClass C p k L)
            (W j) (hW j) (hDim j)).1 x
```

**`Stacks.Chow.effectiveCartierIntersectionOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean#L187). The attribute's comment: “intersection with an effective Cartier divisor”.

> Intersection with the zero scheme of `s`, when that zero scheme is an effective Cartier
> divisor, read as a class on the ambient scheme: the Gysin map of the zero scheme followed by
> proper Chow pushforward along its closed immersion into `X`.

```lean
def effectiveCartierIntersectionOfInvertible
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor (Stacks.Divisors.zeroScheme X L s)) :
    CycleGroup C p (k + 1) →+ chowGroup C p k
```

## Tag 0B70, a remark

[Tag 0B70](https://stacks.math.columbia.edu/tag/0B70) in the Stacks Project.

**`Stacks.Chow.VirtualNormalTriple`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L86). The attribute's comment: “the triple (D, N, σ): D locally principal, N an invertible O\_D-module, σ a surjection from the inverse of N onto the pullback of the ideal sheaf of D”.

> **Remark 0B70.** A triple `(D, 𝒩, σ)` on a scheme `X`: a locally principal closed subscheme
> `i : D ⟶ X`, an invertible `𝒪_D`-module `𝒩` (the virtual normal bundle of `D` in `X`) and a
> surjection `σ : 𝒩^{⊗ -1} ⟶ i^*ℐ_D` of `𝒪_D`-modules.

```lean
structure VirtualNormalTriple (X : Scheme.{u})
```

**`Stacks.Chow.VirtualNormalTriple.normalIsoOfIsEffectiveCartier`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L175). The attribute's comment: “footnote: if D is an effective Cartier divisor, then N is isomorphic to the restriction of O\_X(D) to D”.

> **The footnote of Remark 0B70.** If `D` is an effective Cartier divisor, then
> `𝒩 ≅ 𝒪_X(D)|_D`.

```lean
def normalIsoOfIsEffectiveCartier :
    T.N ≅ (Scheme.Modules.pullback T.D.subschemeι).obj (divisorSheaf T.D)
```

**`Stacks.Chow.virtualNormalGysinOfIdeal_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L427). The attribute's comment: “the construction generalizes Definition 02T8: for D = Z(s) and N isomorphic to the restriction of L the two Gysin maps are equal”.

> **The construction generalizes Definition 02T8.** For the zero scheme `D = Z(s)` of a section
> `s` of an invertible module `ℒ`, and any invertible `𝒪_D`-module `𝒩 ≅ ℒ|_D`, the Gysin map of
> `(D, 𝒩)` is the Gysin map of Definition 02T8.

```lean
theorem virtualNormalGysinOfIdeal_zeroScheme (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (N : (Stacks.Divisors.zeroScheme X L s).subscheme.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible
      (Stacks.Divisors.zeroScheme X L s).subscheme.sheaf.obj
      (Stacks.Divisors.zeroScheme X L s).subscheme.ringCatSheaf.property N]
    (ψ : N ≅ (Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj L) :
    virtualNormalGysinOfIdeal C p k (Stacks.Divisors.zeroScheme X L s) N =
      gysinHomomorphismOfInvertible C p k L s
```

**`Stacks.Chow.VirtualNormalTriple.gysin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L476). The attribute's comment: “the Gysin homomorphism i^* from (k+1)-cycles on X to CH\_k(D) of a triple”.

> **Remark 0B70.** The Gysin homomorphism `i^* : Z_{k+1}(X) ⟶ A_k(D)` of a triple
> `(D, 𝒩, σ)`.

```lean
def gysin : CycleGroup C p (k + 1) →+ chowGroup C (T.D.subschemeι ≫ p) k
```

**`Stacks.Chow.VirtualNormalTriple.gysin_of_not_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L482). The attribute's comment: “rule (1)(a) of Definition 02T8 for a triple: W not contained in D”.

> **Remark 0B70, rule (1)(a) of Definition 02T8 for a triple.** For an integral closed
> subscheme `W ⊆ X` of delta-dimension `k + 1` with `W ⊄ D`, `i^*[W] = [D ∩ W]_k`.

```lean
theorem gysin_of_not_le (W : X.IdealSheafData) (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)) (h : ¬ T.D ≤ W) :
    T.gysin C p k (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
      QuotientAddGroup.mk
        (cycleAssociatedToClosedSubscheme C (T.D.subschemeι ≫ p)
          ((W.comap T.D.subschemeι).subschemeι) k)
```

**`Stacks.Chow.VirtualNormalTriple.gysin_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L494). The attribute's comment: “rule (1)(b) of Definition 02T8 for a triple: W contained in D, with c\_1(N|\_W)”.

> **Remark 0B70, rule (1)(b) of Definition 02T8 for a triple.** For an integral closed
> subscheme `W ⊆ D` of delta-dimension `k + 1`, `i^*[W] = i'_*(c₁(𝒩|_W) ∩ [W])`, where
> `i' : W ⟶ D` is the induced closed immersion.

```lean
theorem gysin_of_le (W : X.IdealSheafData) (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)) (h : T.D ≤ W) :
    T.gysin C p k (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
      properChowPushforward C (W.subschemeι ≫ p) (T.D.subschemeι ≫ p)
        (Scheme.IdealSheafData.inclusion h) (by simp) k
        (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
          (Scheme.IdealSheafData.inclusion h) C (W.subschemeι ≫ p) (T.D.subschemeι ≫ p)
          (by simp) k)
        (virtualNormalChernClass C p k T.D T.N W hW hDim h)
```

**`Stacks.Chow.VirtualNormalTriple.gysin_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L508). The attribute's comment: “rule (2) of Definition 02T8 for a triple: locally finite sums”.

> **Remark 0B70, rule (2) of Definition 02T8 for a triple.** For `α = ∑ n_j [W_j]` locally
> finite, `i^*α = ∑ n_j i^*[W_j]`.

```lean
theorem gysin_finsum {J : Type u} (W : J → X.IdealSheafData)
    (hW : ∀ j, IsIntegral (W j).subscheme)
    (hDim : ∀ j, schemeDeltaDimension C ((W j).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (hLocal : LocallyFinite (fun j ↦ ((W j).support : Set X))) (n : J → ℤ)
    (α : CycleGroup C p (k + 1))
    (hα : ∀ x : X, α.1 x = ∑ᶠ j : J, n j *
      (cycleAssociatedToClosedSubscheme C p (W j).subschemeι (k + 1)).1 x) :
    ∃ β : CycleGroup C (T.D.subschemeι ≫ p) k,
      T.gysin C p k α = QuotientAddGroup.mk β ∧
      ∀ x : T.D.subscheme, β.1 x = ∑ᶠ j : J, n j *
        (gysinComponentCycleOfIdeal C p k (virtualNormalChernRule C p k T.D T.N) T.D
          (W j) (hW j) (hDim j)).1 x
```

**`Stacks.Chow.VirtualNormalTriple.nonempty_normalIso_of_isEffectiveCartier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L526). The attribute's comment: “footnote: if D is an effective Cartier divisor, then N is isomorphic to the restriction of O\_X(D) to D”.

> **The footnote of Remark 0B70.** If `D` is an effective Cartier divisor, then
> `𝒩 ≅ 𝒪_X(D)|_D`.

```lean
theorem nonempty_normalIso_of_isEffectiveCartier (hD : IsEffectiveCartierDivisor T.D) :
    Nonempty (T.N ≅ (Scheme.Modules.pullback T.D.subschemeι).obj (divisorSheaf T.D))
```

**`Stacks.Chow.VirtualNormalTriple.gysin_heq_of_zeroScheme_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L536). The attribute's comment: “the construction generalizes Definition 02T8: agreement when D = Z(s) and N is the restriction of L”.

> **Remark 0B70: the construction generalizes Definition 02T8.** If `D = Z(s)` for a global
> section `s` of an invertible `𝒪_X`-module `ℒ` and `𝒩 ≅ ℒ|_D`, the Gysin map of the triple is the
> Gysin map of Definition 02T8 of `(ℒ, s)`.

```lean
theorem gysin_heq_of_zeroScheme_eq (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (hz : Stacks.Divisors.zeroScheme X L s = T.D)
    (ψ : T.N ≅ (Scheme.Modules.pullback T.D.subschemeι).obj L) :
    HEq (T.gysin C p k) (gysinHomomorphismOfInvertible C p k L s)
```

**`Stacks.Chow.VirtualNormalTriple.gysin_heq_divisorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L547). The attribute's comment: “agreement with Definition 02T8 when D is an effective Cartier divisor”.

> **Remark 0B70 at an effective Cartier divisor.** If `D` is an effective Cartier divisor (so
> that `𝒩 ≅ 𝒪_X(D)|_D` by the footnote), the Gysin map of the triple is the Gysin map of
> Definition 02T8 of `(𝒪_X(D), 1_D)`, whose zero scheme is `D`.

```lean
theorem gysin_heq_divisorSheaf (hD : IsEffectiveCartierDivisor T.D) :
    HEq (T.gysin C p k)
      (gysinHomomorphismOfInvertible C p k (divisorSheaf T.D) (divisorSheafGlobalSection T.D))
```

**`Stacks.Chow.VirtualNormalTriple.chowPushforwardOfIso_gysinHomomorphismOfInvertible_divisorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L581). The attribute's comment: “agreement with Definition 02T8 when D is an effective Cartier divisor, as an identity of Chow classes”.

> **Remark 0B70 at an effective Cartier divisor**, as an identity of Chow classes: the Gysin
> map of Definition 02T8 of `(𝒪_X(D), 1_D)`, transported along `Z(1_D) = D`, is the Gysin map of
> the triple.

```lean
theorem chowPushforwardOfIso_gysinHomomorphismOfInvertible_divisorSheaf
    (hD : IsEffectiveCartierDivisor T.D) (α : CycleGroup C p (k + 1)) :
    chowPushforwardOfIso C
        ((Stacks.Divisors.zeroScheme X (divisorSheaf T.D)
          (divisorSheafGlobalSection T.D)).subschemeι ≫ p) (T.D.subschemeι ≫ p)
        (eqToHom (congrArg Scheme.IdealSheafData.subscheme
          (@zeroScheme_canonicalSection X T.D hD)))
        (by rw [← Category.assoc, eqToHom_subscheme_comp_subschemeι _ _
          (@zeroScheme_canonicalSection X T.D hD)]) k
        (@gysinHomomorphismOfInvertible C X p _ k (divisorSheaf T.D)
          (@isInvertible_divisorSheaf X T.D hD) (divisorSheafGlobalSection T.D) α) =
      T.gysin C p k α
```

**`Stacks.Chow.virtualNormalTriple_remark`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean, line 611](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalTripleGysin.lean#L611). The attribute's comment: “the whole remark: the footnote, the Gysin homomorphism of a triple with the rules of Definition 02T8, and its agreement with Definition 02T8”.

> **Remark 0B70**, all of its assertions together. Let `X` be locally of finite type over the
> base of a Chow situation (Situation 02QL) and let `(D, 𝒩, σ)` be a triple: `D` a locally
> principal closed subscheme, `𝒩` an invertible `𝒪_D`-module and `σ : 𝒩^{⊗ -1} ⟶ i^*ℐ_D` a
> surjection. Then:
> * (footnote) if `D` is an effective Cartier divisor, `𝒩 ≅ 𝒪_X(D)|_D`, and every effective Cartier
>   divisor carries such a triple;
> * the Gysin homomorphism `i^* : Z_{k+1}(X) ⟶ A_k(D)` of the triple obeys the rules of
>   Definition 02T8 with `𝒩` in place of `ℒ|_D`: `i^*[W] = [D ∩ W]_k` for `W ⊄ D`,
>   `i^*[W] = i'_*(c₁(𝒩|_W) ∩ [W])` for `W ⊆ D`, and `i^*(∑ n_j [W_j]) = ∑ n_j i^*[W_j]`;
> * it generalizes Definition 02T8: for `D = Z(s)` and `𝒩 ≅ ℒ|_D` it is the Gysin map of `(ℒ, s)`,
>   and for `D` an effective Cartier divisor it is the Gysin map of `(𝒪_X(D), 1_D)`.

```lean
theorem virtualNormalTriple_remark (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] :
    (∀ T : VirtualNormalTriple X, IsEffectiveCartierDivisor T.D →
      Nonempty (T.N ≅ (Scheme.Modules.pullback T.D.subschemeι).obj (divisorSheaf T.D))) ∧
    (∀ D : X.IdealSheafData, IsEffectiveCartierDivisor D →
      ∃ T : VirtualNormalTriple X, T.D = D) ∧
    (∀ (k : ℤ) (T : VirtualNormalTriple X) (W : X.IdealSheafData), IsIntegral W.subscheme →
      schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt) →
      ¬ T.D ≤ W →
      T.gysin C p k (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
        QuotientAddGroup.mk
          (cycleAssociatedToClosedSubscheme C (T.D.subschemeι ≫ p)
            ((W.comap T.D.subschemeι).subschemeι) k)) ∧
    (∀ (k : ℤ) (T : VirtualNormalTriple X) (W : X.IdealSheafData) (hW : IsIntegral W.subscheme)
      (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
      (h : T.D ≤ W),
      T.gysin C p k (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
        properChowPushforward C (W.subschemeι ≫ p) (T.D.subschemeι ≫ p)
          (Scheme.IdealSheafData.inclusion h) (by simp) k
          (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
            (Scheme.IdealSheafData.inclusion h) C (W.subschemeι ≫ p) (T.D.subschemeι ≫ p)
            (by simp) k)
          (virtualNormalChernClass C p k T.D T.N W hW hDim h)) ∧
    (∀ (k : ℤ) (T : VirtualNormalTriple X) {J : Type u} (W : J → X.IdealSheafData)
      (hW : ∀ j, IsIntegral (W j).subscheme)
      (hDim : ∀ j, schemeDeltaDimension C ((W j).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)),
      LocallyFinite (fun j ↦ ((W j).support : Set X)) → ∀ (n : J → ℤ)
      (α : CycleGroup C p (k + 1)),
      (∀ x : X, α.1 x = ∑ᶠ j : J, n j *
        (cycleAssociatedToClosedSubscheme C p (W j).subschemeι (k + 1)).1 x) →
      ∃ β : CycleGroup C (T.D.subschemeι ≫ p) k,
        T.gysin C p k α = QuotientAddGroup.mk β ∧
        ∀ x : T.D.subscheme, β.1 x = ∑ᶠ j : J, n j *
          (gysinComponentCycleOfIdeal C p k (virtualNormalChernRule C p k T.D T.N) T.D
            (W j) (hW j) (hDim j)).1 x) ∧
    (∀ (k : ℤ) (T : VirtualNormalTriple X) (L : X.Modules)
      [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
      (s : Γ(L, ⊤)), Stacks.Divisors.zeroScheme X L s = T.D →
      (T.N ≅ (Scheme.Modules.pullback T.D.subschemeι).obj L) →
      HEq (T.gysin C p k) (gysinHomomorphismOfInvertible C p k L s)) ∧
    (∀ (k : ℤ) (T : VirtualNormalTriple X) [IsEffectiveCartierDivisor T.D],
      HEq (T.gysin C p k)
        (gysinHomomorphismOfInvertible C p k (divisorSheaf T.D)
          (divisorSheafGlobalSection T.D)))
```

## Tag 02T9, a lemma

[Tag 02T9](https://stacks.math.columbia.edu/tag/02T9) in the Stacks Project.

**`Stacks.Chow.properChowPushforward_gysinHomomorphismOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinPushforwardChernCap.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinPushforwardChernCap.lean#L255).

> **Stacks 02T9.** Pushing the Gysin class of the zero scheme `i : D = Z(s) ⟶ X` forward to `X`
> is capping with the first Chern class of `L`: `i_* i^* α = c₁(L) ∩ α` in `A_k(X)` for every
> `α ∈ Z_{k+1}(X)`.
>
> The vanishing of Stacks 02S2 that `Stacks.Chow.properChowPushforward` requires is supplied, not
> assumed, the zero scheme being a closed subscheme of `X`.

```lean
theorem properChowPushforward_gysinHomomorphismOfInvertible (α : CycleGroup C p (k + 1)) :
    properChowPushforward C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p
        (Stacks.Divisors.zeroScheme X L s).subschemeι rfl k
        (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
          (Stacks.Divisors.zeroScheme X L s).subschemeι C
          ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p rfl k)
        (gysinHomomorphismOfInvertible C p k L s α) =
      firstChernClassCapOfInvertible C p k L α
```

**`Stacks.Chow.effectiveCartierIntersection_divisorSheaf_eq_firstChernClassCapOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinPushforwardChernCap.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinPushforwardChernCap.lean#L388). The attribute's comment: “in particular”.

> **Stacks 02T9, the "in particular" clause for a given effective Cartier divisor.** For an
> effective Cartier divisor `D` on `X`, intersection with `D` — taken through the canonical section
> `1_D` of `𝒪_X(D)`, whose zero scheme is `D` — is capping with `c₁(𝒪_X(D))`.
>
> The effective Cartier hypothesis of `Stacks.Chow.effectiveCartierIntersection` is carried but
> unused by that construction, so transporting it along `Z(1_D) = D` (Stacks 01X0) costs nothing.

```lean
theorem effectiveCartierIntersection_divisorSheaf_eq_firstChernClassCapOfInvertible
    (D : X.IdealSheafData) [hD : Stacks.Divisors.IsEffectiveCartierDivisor D]
    (α : CycleGroup C p (k + 1)) :
    effectiveCartierIntersectionOfInvertible C p k (Stacks.Divisors.divisorSheaf D)
        (Stacks.Divisors.divisorSheafGlobalSection D)
        (isEffectiveCartierDivisor_zeroScheme_divisorSheaf D) α =
      firstChernClassCapOfInvertible C p k (Stacks.Divisors.divisorSheaf D) α
```

## Tag 02TB, a lemma

[Tag 02TB](https://stacks.math.columbia.edu/tag/02TB) in the Stacks Project.

**`Stacks.Chow.gysinHomomorphismOfInvertible_cycleAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinCartierIntersection/ClosedSubschemeCycle.lean, line 712](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinCartierIntersection/ClosedSubschemeCycle.lean#L712). The attribute's comment: “part (1)”.

> Intersecting a closed subscheme properly with a Cartier zero scheme computes
> its Gysin class.

```lean
theorem gysinHomomorphismOfInvertible_cycleAssociatedToClosedSubscheme
    (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (k : ℤ)
    (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections) (Z : X.IdealSheafData)
    (hZ : schemeDeltaDimension C (Z.subschemeι ≫ p) ≤
      ((k + 1 : ℤ) : EInt))
    (hDZ : Stacks.Divisors.IsEffectiveCartierDivisor
      ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).comap Z.subschemeι)) :
    gysinHomomorphismOfInvertible C p k L (s.eval (.op ⊤))
        (cycleAssociatedToClosedSubscheme C p Z.subschemeι (k + 1)) =
      QuotientAddGroup.mk
        (cycleAssociatedToClosedSubscheme C
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)
          ((Z.comap (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι).subschemeι)
            k)
```

**`Stacks.Chow.schemeDeltaDimension_pullback_support_le_of_mono_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinCoherentSheaf.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinCoherentSheaf.lean#L1081). The attribute's comment: “part (2): support bound”.

> The support of a coherent sheaf on which a Cartier section is regular
> loses at least one dimension upon restriction to the zero scheme.

```lean
theorem schemeDeltaDimension_pullback_support_le_of_mono_section
    (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (k : ℤ)
    (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections) (F : X.Modules) [F.IsCoherent]
    (hF : schemeDeltaDimension C
      ((reducedSupport F).subschemeι ≫ p) ≤
        ((k + 1 : ℤ) : EInt))
    (hs : Mono (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩)).map (((𝟙 F), (L.unitHomEquiv.symm s)) : (_, _) ⟶ (_, _))))) :
    schemeDeltaDimension C
      ((@reducedSupport _
          ((Scheme.Modules.pullback
            (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι).obj F)
          (@AlgebraicGeometry.isCoherent_pullback
            (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subscheme X
            (LocallyOfFiniteType.isLocallyNoetherian
              ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p))
            (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι F
            inferInstance)).subschemeι ≫
        (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p) ≤ (k : EInt)
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_cycleAssociatedToCoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinCoherentSheaf.lean, line 1121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinCoherentSheaf.lean#L1121). The attribute's comment: “part (2): Gysin formula”.

> Gysin pullback of the associated cycle of a coherent sheaf on which the
> section is regular is the associated cycle of its restriction.

```lean
theorem gysinHomomorphismOfInvertible_cycleAssociatedToCoherentSheaf
    (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (k : ℤ)
    (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections) (F : X.Modules) [F.IsCoherent]
    (hF : schemeDeltaDimension C
      ((reducedSupport F).subschemeι ≫ p) ≤
        ((k + 1 : ℤ) : EInt))
    (hs : Mono (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩)).map (((𝟙 F), (L.unitHomEquiv.symm s)) : (_, _) ⟶ (_, _))))) :
    gysinHomomorphismOfInvertible C p k L (s.eval (.op ⊤))
        (cycleAssociatedToCoherentSheaf C p F
          (k + 1) hF) =
      QuotientAddGroup.mk
        (@cycleAssociatedToCoherentSheaf _ C
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p) inferInstance
          ((Scheme.Modules.pullback
            (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι).obj F)
          (@AlgebraicGeometry.isCoherent_pullback
            (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subscheme X
            (LocallyOfFiniteType.isLocallyNoetherian
              ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p))
            (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι F
            inferInstance) k
          (by
            exact schemeDeltaDimension_pullback_support_le_of_mono_section
              C p k L s F hF hs))
```

## Tag 0B6Z, a remark

[Tag 0B6Z](https://stacks.math.columbia.edu/tag/0B6Z) in the Stacks Project.

**`Stacks.Chow.gysinCycleMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean#L295). The attribute's comment: “the canonical map on cycles”.

> The canonical Gysin map on cycles `i^* : Z_{k+1}(X) ⟶ Z_k(D)` attached to a section `s` of an
> invertible module whose restriction to the zero scheme `D = Z(s)` is trivial: the extension of
> the two rules of `Stacks.Chow.gysinCycleMapComponent` over locally finite presentations by
> integral closed subschemes. It does not depend on a trivialization of `L|_D`.

```lean
def gysinCycleMap
    (_htriv : AlgebraicGeometry.SheafOfModules.IsTrivial
      (Stacks.Divisors.zeroScheme X L s).subscheme.sheaf.obj
      (Stacks.Divisors.zeroScheme X L s).subscheme.ringCatSheaf.property
      ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj L)) :
    CycleGroup C p (k + 1) →+
      CycleGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
```

**`Stacks.Chow.gysinCycleMap_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean#L312). The attribute's comment: “vanishing on integral closed subschemes contained in the zero scheme”.

> An integral closed subscheme contained in the zero scheme has zero image under the canonical
> map on cycles.

```lean
theorem gysinCycleMap_of_le (W : X.IdealSheafData) (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (h : Stacks.Divisors.zeroScheme X L s ≤ W) :
    gysinCycleMap C p k L s htriv
      (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) = 0
```

**`Stacks.Chow.gysinCycleMap_of_not_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean#L325). The attribute's comment: “agreement with Stacks 02T8 off the zero scheme”.

> The canonical map on cycles sends an integral closed subscheme `W` not contained in `D` to the
> fundamental cycle of the scheme-theoretic intersection `W ∩ D`.

```lean
theorem gysinCycleMap_of_not_le (W : X.IdealSheafData) (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (h : ¬ Stacks.Divisors.zeroScheme X L s ≤ W) :
    gysinCycleMap C p k L s htriv
        (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
      cycleAssociatedToClosedSubscheme C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
        ((W.comap (Stacks.Divisors.zeroScheme X L s).subschemeι).subschemeι) k
```

**`Stacks.Chow.isGysinCycleMap_gysinCycleMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean#L356). The attribute's comment: “the locally finite component formula”.

> The canonical map on cycles satisfies the locally finite component formula.

```lean
theorem isGysinCycleMap_gysinCycleMap :
    IsGysinCycleMap C p k L s (gysinCycleMap C p k L s htriv)
```

**`Stacks.Chow.eq_gysinCycleMap_of_isGysinCycleMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestriction.lean#L365). The attribute's comment: “canonicity”.

> Any additive map `Z_{k+1}(X) ⟶ Z_k(D)` satisfying the locally finite component formula is the
> canonical map on cycles.

```lean
theorem eq_gysinCycleMap_of_isGysinCycleMap
    (F : CycleGroup C p (k + 1) →+
      CycleGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k)
    (hF : IsGysinCycleMap C p k L s F) :
    F = gysinCycleMap C p k L s htriv
```

## Tag 0B6Y, a remark

[Tag 0B6Y](https://stacks.math.columbia.edu/tag/0B6Y) in the Stacks Project.

**`Stacks.Divisors.zeroScheme_pullback_comp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/BaseChangeComparison.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/BaseChangeComparison.lean#L68). The attribute's comment: “the zero scheme of a section pulled back along a composite does not depend on the factorization”.

> **Stacks 0B6Y.** The zero scheme of a section pulled back to `A` depends only on the morphism
> `A ⟶ T`, not on a factorization of it: two factorizations `q₁ ≫ q₂ = r₁ ≫ r₂` give equal zero
> schemes, both being the inverse image of `Z(s)` along that morphism.

```lean
theorem zeroScheme_pullback_comp_comp {A B B' T : Scheme.{u}} (q₁ : A ⟶ B) (q₂ : B ⟶ T)
    (r₁ : A ⟶ B') (r₂ : B' ⟶ T) (h : q₁ ≫ q₂ = r₁ ≫ r₂) (L : T.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible T.sheaf.obj T.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) :
    zeroScheme A ((Scheme.Modules.pullback q₁).obj ((Scheme.Modules.pullback q₂).obj L))
        (AlgebraicGeometry.pullbackGlobalSections q₁ ((Scheme.Modules.pullback q₂).obj L)
          (AlgebraicGeometry.pullbackGlobalSections q₂ L s)) =
      zeroScheme A ((Scheme.Modules.pullback r₁).obj ((Scheme.Modules.pullback r₂).obj L))
        (AlgebraicGeometry.pullbackGlobalSections r₁ ((Scheme.Modules.pullback r₂).obj L)
          (AlgebraicGeometry.pullbackGlobalSections r₂ L s))
```

**`Stacks.Divisors.zeroScheme_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean#L109). The attribute's comment: “the pulled-back zero scheme”.

> **Stacks 0B6Y.** The zero scheme of the pulled-back section is the scheme-theoretic inverse
> image of the zero scheme: `Z(f^* s) = f⁻¹(Z(s))` as quasi-coherent ideal sheaves on `X'`.
>
> Together with `AlgebraicGeometry.Scheme.IdealSheafData.comapIso` and its two projection
> identities this is the cartesian square `Z(f^* s) ≅ X' ×_X Z(s)` of the tag.

```lean
theorem zeroScheme_pullback {X X' : Scheme.{u}} (f : X' ⟶ X) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) :
    zeroScheme X' ((Scheme.Modules.pullback f).obj L) (pullbackGlobalSections f L s) =
      (zeroScheme X L s).comap f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.IdealSheafData.comapIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData.comapIso#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean#L159) (StacksFrontier): “the cartesian square”. References: EGA IV (19.4.1), “more general”.
- [`AlgebraicGeometry.Scheme.IdealSheafData.comapIso_hom_fst`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData.comapIso_hom_fst#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean#L161) (StacksFrontier): “the pulled-back inclusion”. References: EGA I (4.4.1), “closed case”.
- [`AlgebraicGeometry.Scheme.IdealSheafData.comapIso_hom_snd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData.comapIso_hom_snd#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Basic.lean#L164) (StacksFrontier): “the map to the original zero scheme”.

## Tag 02TA, a lemma

[Tag 02TA](https://stacks.math.columbia.edu/tag/02TA) in the Stacks Project.

**`Stacks.Chow.canonicalGysinSystem_isNaturalUnderInverseIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean#L370). The attribute's comment: “the inverse-isomorphism case of the naturality of the Gysin operation, for the canonical Gysin system of Stacks 02TO, with no hypothesis”.

> **The canonical Gysin system is natural under inverse isomorphisms**: the inverse-isomorphism
> case of the naturality of the Gysin operation.

```lean
theorem canonicalGysinSystem_isNaturalUnderInverseIso (C : ChowSituation.{u}) :
    (canonicalGysinSystem C).IsNaturalUnderInverseIso
```

**`Stacks.Chow.canonicalGysinSystem_isNaturalUnderBaseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean#L378). The attribute's comment: “the base-change-isomorphism case of the naturality of the Gysin operation, for the canonical Gysin system of Stacks 02TO, with no hypothesis”.

> **The canonical Gysin system is natural under base-change isomorphisms**: the
> base-change-isomorphism case of the naturality of the Gysin operation.

```lean
theorem canonicalGysinSystem_isNaturalUnderBaseChangeIso (C : ChowSituation.{u}) :
    (canonicalGysinSystem C).IsNaturalUnderBaseChangeIso
```

**`Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderBaseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean#L101). The attribute's comment: “the isomorphism case of the naturality of the Gysin operation of a Gysin system, for an invertible module pulled back from a test scheme to both schemes -- the form the Gysin axiom of a bivariant class quantifies over -- with no hypothesis”.

> The Gysin system of the first Chern class rule of an invertible module is natural under
> pushforward along an isomorphism `u : A ⟶ B` of two schemes over a test scheme carrying the module,
> the module on `A` and on `B` being its pullbacks from the test scheme.

```lean
theorem gysinSystemOfInvertible_isNaturalUnderBaseChangeIso (C : ChowSituation.{u}) :
    (gysinSystemOfInvertible C).IsNaturalUnderBaseChangeIso
```

**`Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpensRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean#L425). The attribute's comment: “the open-immersion case of the naturality of the Gysin operation of a Gysin system, for an invertible module on the ambient scheme: restriction along an open immersion over the base carries the Gysin map of Z(s) to the Gysin map of Z(u^*s) across the square of Remark 0B6Y, with no hypothesis”.

> **The open-immersion case of Stacks 02TA for the Gysin operation of a Gysin system, with the
> module on the ambient scheme.** The Gysin system of the first Chern class rule of an invertible
> module is natural under restriction along an open immersion over the base, with no hypothesis.
>
> Its Gysin operation is `Stacks.Chow.gysinHomomorphismOnChowOfInvertible`, so this is
> `Stacks.Chow.chowGroupRestrict_gysinHomomorphismOnChowOfInvertible_of_eq`, the open-immersion case
> of Stacks 0B71 at that map, after the quantified open immersion of the two zero schemes is
> identified with the morphism of Remark 0B6Y by `Stacks.Chow.eq_zeroSchemePullbackHom`.

```lean
theorem gysinSystemOfInvertible_isNaturalUnderOpensRestriction (C : ChowSituation.{u}) :
    (gysinSystemOfInvertible C).IsNaturalUnderOpensRestriction
```

**`Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean#L465). The attribute's comment: “the open-immersion case of the naturality of the Gysin operation of a Gysin system, for an invertible module pulled back from a test scheme to both schemes -- the form the Gysin axiom of a bivariant class quantifies over -- with no hypothesis”.

> **The open-immersion case of Stacks 02TA for the Gysin operation of a Gysin system.** The
> Gysin system of the first Chern class rule of an invertible module is natural under restriction
> along an open immersion `u : A ⟶ B` of schemes over a test scheme carrying the module, with no
> hypothesis.
>
> The module on `A` is the pullback of the module on the test scheme, not the pullback along `u` of
> the module on `B`, so this is not the ambient-module form
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpensRestriction` but its composite with the
> comparison of the two spellings,
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderPullbackComp`: the quantified open immersion of
> the two zero schemes factors as the transport along
> `Stacks.Chow.zeroScheme_pullback_pullback` followed by the morphism of Remark 0B6Y, uniquely
> because the closed immersion of the zero scheme downstairs is a monomorphism.

```lean
theorem gysinSystemOfInvertible_isNaturalUnderOpenImmersion (C : ChowSituation.{u}) :
    (gysinSystemOfInvertible C).IsNaturalUnderOpenImmersion
```

**`Stacks.Chow.GenuineChern.gysinSystemOfInvertible_isNaturalUnderInverseIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/InverseIsoGysin.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/InverseIsoGysin.lean#L64). The attribute's comment: “the inverse-isomorphism case of the naturality of the Gysin operation of a Gysin system, for the system of the first Chern class rule of an invertible module”.

> **The isomorphism case of Stacks 02TA for the Gysin system of the first Chern class rule**,
> with the invertible module on the source of the isomorphism: for an isomorphism `u : A ⟶ B` over
> the base with inverse `w`, an invertible module `L` on `A`, a section `s` of it and a morphism `j`
> of zero schemes lying over `u`, the Gysin map of `(w^*L, w^*s)` on `B` applied to `u_*α` is
> `j_*` of the Gysin map of `(L, s)` on `A` applied to `α`.
>
> Stacks 02TA for the proper morphism `w` and the module `L` on `A` itself,
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderProperPushforward`, gives
> `i^* w_* β = (j'')_* (i')^* β` for the morphism `j''` of Remark 0B6Y; at `β = u_* α` the left
> side collapses since `u ≫ w = 𝟙`, and `j'' ≫ j = 𝟙` because `j` lies over `u` and a closed
> immersion is a monomorphism.

```lean
theorem gysinSystemOfInvertible_isNaturalUnderInverseIso (C : ChowSituation.{u}) :
    (gysinSystemOfInvertible C).IsNaturalUnderInverseIso
```

**`Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderProperPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ProperPushforwardGysinSystem.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ProperPushforwardGysinSystem.lean#L121). The attribute's comment: “the naturality of the Gysin operation of a Gysin system under pushforward along a general proper morphism”.

> The Gysin system of the first Chern class rule of an invertible module is natural under
> pushforward along an arbitrary proper morphism over the base.

```lean
theorem gysinSystemOfInvertible_isNaturalUnderProperPushforward (C : ChowSituation.{u}) :
    (gysinSystemOfInvertible C).IsNaturalUnderProperPushforward
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_properPushforward_of_gysinCompatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ProperPushforwardInvertible.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ProperPushforwardInvertible.lean#L274). The attribute's comment: “the identity i^* f\_* α' = g\_* (i')^* α' in A\_k(Z(s)) over the square of Remark 0B6Y, for the Gysin map of an invertible module and a global section, with no hypothesis beyond properness of f and the commutativity of f over the base”.

> **Stacks 02TA.** Gysin pullback through the zero scheme of a global section of an invertible
> module commutes with proper pushforward across the square of Remark 0B6Y:
>
>   `i^* f_* α' = g_* (i')^* α'`  in  `A_k(Z(s))`,  for every `α' ∈ Z_{k+1}(X')`.
>
> Both Gysin maps are `Stacks.Chow.gysinHomomorphismOfInvertible`, functions of the invertible
> module and the section alone; the morphism `g` of Remark 0B6Y is
> `Stacks.Chow.zeroSchemePullbackHom`; and the instance of Stacks 02S2 that
> `Stacks.Chow.properChowPushforward` requires along `g` is supplied by
> `Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence`. Nothing is assumed beyond the
> properness of `f` and the commutativity of `f` over the base.
>
> Both sides are classes of cycles on `Z(s)`, and the two cycles are rationally equivalent by
> `Stacks.Chow.rationallyEquivalent_gysinRule_extendCycleGroup_properPushforward`.

```lean
theorem gysinHomomorphismOfInvertible_properPushforward_of_gysinCompatible [IsProper f]
    (hf : f ≫ p = p') (α : CycleGroup C p' (k + 1)) :
    gysinHomomorphismOfInvertible C p k L s (properPushforward C p' p f hf (k + 1) α) =
      properChowPushforward C ((pullbackZeroScheme f L s).subschemeι ≫ p')
        ((zeroScheme X L s).subschemeι ≫ p) (zeroSchemePullbackHom f L s)
        (zeroSchemePullbackHom_comp f L s C p p' hf) k
        (properPushforwardFactorsThroughRationalEquivalence C
          ((pullbackZeroScheme f L s).subschemeι ≫ p')
          ((zeroScheme X L s).subschemeι ≫ p) (zeroSchemePullbackHom f L s)
          (zeroSchemePullbackHom_comp f L s C p p' hf) k)
        (gysinHomomorphismOfInvertible C p' k ((Scheme.Modules.pullback f).obj L)
          (AlgebraicGeometry.pullbackGlobalSections f L s) α)
```

## Tag 0B71, a lemma

[Tag 0B71](https://stacks.math.columbia.edu/tag/0B71) in the Stacks Project.

**`Stacks.Chow.gysinHomomorphismOfInvertible_flatPullback_cycleAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/FlatPullbackInvertible.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/FlatPullbackInvertible.lean#L220). The attribute's comment: “closed subscheme meeting the zero scheme properly; 02S1 along g carried”.

> **Stacks 0B71 on the fundamental cycle of a closed subscheme meeting the zero scheme
> properly.** For a closed subscheme `Z ⊆ X` of delta-dimension at most `k + 1` whose intersection
> with `D = Z(s)` is an effective Cartier divisor on `Z`, and whose inverse image `f^{-1}Z` meets
> `D' = Z(f^*s)` in the same way,
>
>   `(i')^* f^* [Z]_{k+1} = g^* i^* [Z]_{k+1}`  in  `CH_{k+r}(D')`.
>
> Here `i^*` and `(i')^*` are the Gysin maps `Stacks.Chow.gysinHomomorphismOfInvertible` of
> Stacks 02T8 for `(L, s)` and for `(f^*L, f^*s)`, `f^*` is the flat pullback of cycles of
> Stacks 02RB, and `g^*` is the flat pullback on Chow groups of Stacks 0FVK along the comparison
> morphism `Stacks.Chow.zeroSchemePullbackHom` of Remark 0B6Y, whose flatness and relative dimension
> are supplied by the cartesian square and are **not** hypotheses. No first Chern class component
> rule is a parameter, and the invertibility of `f^*L` is an instance.
>
> This is the first case of the source's proof, for an arbitrary closed subscheme rather than only
> an integral one. Carried: the vanishing of **Stacks 02S1** along `g`, without which the right hand
> side does not exist, and the five side conditions of Stacks 02TB (1) and Stacks 02RB at the two
> schemes of the square; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.Gysin42.FlatPullbackInvertible`.

```lean
theorem gysinHomomorphismOfInvertible_flatPullback_cycleAssociatedToClosedSubscheme
    (Z : X.IdealSheafData)
    (hZ : schemeDeltaDimension C (Z.subschemeι ≫ p) ≤ ((k + 1 : ℤ) : EInt))
    (hDZ : Stacks.Divisors.IsEffectiveCartierDivisor
      ((Stacks.Divisors.zeroScheme X L s).comap Z.subschemeι))
    (hZ' : schemeDeltaDimension C ((Z.comap f).subschemeι ≫ (f ≫ p)) ≤
      ((k + (r : ℤ) + 1 : ℤ) : EInt))
    (hDZ' : Stacks.Divisors.IsEffectiveCartierDivisor
      ((pullbackZeroScheme f L s).comap (Z.comap f).subschemeι))
    (hZD : schemeDeltaDimension C
      ((Z.comap (Stacks.Divisors.zeroScheme X L s).subschemeι).subschemeι ≫
        ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)) ≤ (k : EInt))
    (hfac : FlatPullbackFactorsThroughRationalEquivalence C
      ((pullbackZeroScheme f L s).subschemeι ≫ (f ≫ p))
      ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (zeroSchemePullbackHom f L s)
      (zeroSchemePullbackHom_comp f L s C p (f ≫ p) rfl) r
      (relativeDimension_zeroSchemePullbackHom f L s r hf) k) :
    gysinHomomorphismOfInvertible C (f ≫ p) (k + (r : ℤ))
        ((Scheme.Modules.pullback f).obj L) (pullbackGlobalSections f L s)
        ((show k + 1 + (r : ℤ) = k + (r : ℤ) + 1 by omega) ▸
          flatPullback C (f ≫ p) p f rfl r hf (k + 1)
            (cycleAssociatedToClosedSubscheme C p Z.subschemeι (k + 1))) =
      flatPullbackChow C ((pullbackZeroScheme f L s).subschemeι ≫ (f ≫ p))
        ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (zeroSchemePullbackHom f L s)
        (zeroSchemePullbackHom_comp f L s C p (f ≫ p) rfl) r
        (relativeDimension_zeroSchemePullbackHom f L s r hf) k hfac
        (gysinHomomorphismOfInvertible C p k L s
          (cycleAssociatedToClosedSubscheme C p Z.subschemeι (k + 1)))
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_flatPullback_of_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/FlatPullbackRationallyCompatible.lean, line 1260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/FlatPullbackRationallyCompatible.lean#L1260). The attribute's comment: “the Gysin map commutes with flat pullback, (i')^* f^* = g^* i^* on A\_\{k+r}(D'), with no hypothesis: the component identity is replaced by its rational-equivalence form, proved here, and the vanishing of 02S1 along g by the general theorem”.

> **Stacks 0B71 for an arbitrary cycle at the Gysin map of an invertible module, with no
> hypothesis.** Gysin pullback through the zero scheme of a section of an invertible module
> commutes with flat pullback:
>
>   `(i')^* f^* α = g^* i^* α`  in  `CH_{k+r}(D')`,  for every `α ∈ Z_{k+1}(X)`.
>
> This is `Stacks.Chow.gysinHomomorphismOfInvertible_flatPullback` with both of its remaining
> hypotheses discharged: the vanishing of Stacks 02S1 along `g` is
> `Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_general`, and the identity on integral
> components is replaced by its rational-equivalence form
> `Stacks.Chow.gysinRationallyCompatibleWithFlatPullback_invertible`, which is proved here. Both
> Gysin maps are `Stacks.Chow.gysinHomomorphismOfInvertible`, no component rule is a parameter, the
> invertibility of `f^*L` is an instance, and `g` is the canonical comparison morphism of Remark
> 0B6Y.

```lean
theorem gysinHomomorphismOfInvertible_flatPullback_of_invertible (α : CycleGroup C p (k + 1)) :
    gysinHomomorphismOfInvertible C (f ≫ p) (k + (r : ℤ)) ((Scheme.Modules.pullback f).obj L)
        (AlgebraicGeometry.pullbackGlobalSections f L s)
        ((show k + 1 + (r : ℤ) = k + (r : ℤ) + 1 by omega) ▸
          flatPullback C (f ≫ p) p f rfl r hf (k + 1) α) =
      flatPullbackChow C ((pullbackZeroScheme f L s).subschemeι ≫ (f ≫ p))
        ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (zeroSchemePullbackHom f L s)
        (zeroSchemePullbackHom_comp f L s C p (f ≫ p) rfl) r
        (relativeDimension_zeroSchemePullbackHom f L s r hf) k
        (flatPullbackFactorsThroughRationalEquivalence_general C
          ((pullbackZeroScheme f L s).subschemeι ≫ (f ≫ p))
          ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (zeroSchemePullbackHom f L s)
          (zeroSchemePullbackHom_comp f L s C p (f ≫ p) rfl) r
          (relativeDimension_zeroSchemePullbackHom f L s r hf) k)
        (gysinHomomorphismOfInvertible C p k L s α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.29, Tag 02T7](https://stacks.math.columbia.edu/tag/02T7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
