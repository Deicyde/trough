---
declaration: section
origin: cited
lean: AlgebraicGeometry.VanishingSituation, AlgebraicGeometry.VanishingSituation.exists_isAdmissibleBlowup_dominating_of_noetherian, AlgebraicGeometry.VanishingSituation.exists_isAdmissibleBlowup_dominating, AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization, AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization_of_le_topologicalKrullDim_specialFiber, AlgebraicGeometry.VanishingSituation.invertibleCurveDegree_conormalOnComponent_pos, AlgebraicGeometry.VanishingSituation.not_isTrivial_conormalSheaf, AlgebraicGeometry.VanishingSituation.exists_subset_invertibleCurveDegree_conormalOnComponent_pos
statement: formalized
proof: formalized
---

# 54.7 Vanishing

Section 54.7 of the Stacks Project, [Tag 0AX7](https://stacks.math.columbia.edu/tag/0AX7). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AX8, a situation

[Tag 0AX8](https://stacks.math.columbia.edu/tag/0AX8) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/Basic.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/Basic.lean#L49).

> **Stacks Project, Tag 0AX8.** The standing data for the vanishing results: a
> two-dimensional Noetherian normal local domain, a modification of its spectrum, and an
> enumeration of the irreducible components of the special fibre.

```lean
structure VanishingSituation
```

## Tag 0B4M, a lemma

[Tag 0B4M](https://stacks.math.columbia.edu/tag/0B4M) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.exists_isAdmissibleBlowup_dominating_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/StrictTransformOpenImmersion.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/StrictTransformOpenImmersion.lean#L134).

> In a `VanishingSituation` there is a `U`-admissible blowup `b : S' ⟶ S` of the punctured
> spectrum `U = S ∖ {s}` which dominates `X`: it factors as `S' ⟶ X ⟶ S`.

```lean
theorem exists_isAdmissibleBlowup_dominating_of_noetherian (V : VanishingSituation.{u}) :
    ∃ (S' : Scheme.{u}) (b : S' ⟶ V.base),
      Stacks.Blowup.IsAdmissibleBlowup V.puncturedSpectrumOpen b ∧
        ∃ g : S' ⟶ V.X, g ≫ V.f = b
```

**`AlgebraicGeometry.VanishingSituation.exists_isAdmissibleBlowup_dominating`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DominatingBlowup.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DominatingBlowup.lean#L312). The attribute's comment: “the case of the cited 081T at Situation 0AX8's modification; 081T's own carried inputs 080Y and 081S are passed through as hypotheses”.

> **Stacks Project, Tag 0B4M.** In Situation [Stacks, Tag 0AX8] there is a `U`-admissible
> blowup `b : S' ⟶ S` of the punctured spectrum `U = S ∖ {s}` which dominates `X`: it factors as
> `S' ⟶ X ⟶ S`.
>
> This is the case of [Stacks, Tag 081T] at the modification `f`, which is an isomorphism over `U`
> by `isIso_morphismRestrict_puncturedSpectrumOpen`. The two hypotheses are the cited results
> [Stacks, Tag 080Y] and [Stacks, Tag 081S] that 081T carries, passed through
> unchanged.

```lean
public theorem exists_isAdmissibleBlowup_dominating (V : VanishingSituation.{u})
    (h080Y : CartierBoundaryReduction V.base V.puncturedSpectrumOpen)
    (h081S : StrictTransformOpenImmersion V.f V.puncturedSpectrumOpen) :
    ∃ (S' : Scheme.{u}) (b : S' ⟶ V.base),
      Stacks.Blowup.IsAdmissibleBlowup V.puncturedSpectrumOpen b ∧
        ∃ g : S' ⟶ V.X, g ≫ V.f = b
```

## Tag 0AX9, a lemma

[Tag 0AX9](https://stacks.math.columbia.edu/tag/0AX9) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorization.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorization.lean#L427). The attribute's comment: “under the standing observation following Situation 0AX8 that every irreducible component of the special fibre has dimension one”.

> A nonzero element of the maximal ideal which, along every irreducible component of the special
> fibre, admits at some closed point of that component and of no other a factorization one factor of
> which lies in the local maximal ideal and restricts to a nonzero function on the component.

```lean
theorem exists_ne_zero_mem_maximalIdeal_factorization
    (V : VanishingSituation.{u})
    (hdim : ∀ i : Fin V.numberOfComponents, topologicalKrullDim (V.component i) = 1) :
    ∃ a : V.A, a ≠ 0 ∧ a ∈ V.maximalIdeal ∧
      ∀ i : Fin V.numberOfComponents,
        ∃ y : componentScheme V i,
          IsClosed
              ({(Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y} : Set V.X) ∧
          (Scheme.IdealSheafData.vanishingIdeal
              (componentClosed V i)).subschemeι y ∈ componentInSource V i ∧
          (∀ j : Fin V.numberOfComponents, j ≠ i →
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y ∉ componentInSource V j) ∧
          ∃ g h : V.X.presheaf.stalk
              ((Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y),
            g ∈ IsLocalRing.maximalIdeal _ ∧
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι.stalkMap y g ≠ 0 ∧
            ((StructureSheaf.toStalk V.A (V.f _) ≫ V.f.stalkMap _) a = g * h)
```

**`AlgebraicGeometry.VanishingSituation.exists_ne_zero_mem_maximalIdeal_factorization_of_le_topologicalKrullDim_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorizationSupplement.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ComponentFactorizationSupplement.lean#L64). The attribute's comment: “the lemma under the standing exclusion of Section 54.7 (Situation 0AX8): the case dim X\_s = 0, discarded by the source, which notes there that f is then finite and hence an isomorphism. The geometric connectedness of the special fibre that the source reads off the Stein factorization is proved here where it is used: a zero-dimensional component is a point open in the special fibre, so Zariski's main theorem over the local base makes the modification an isomorphism and the special fibre a single point, which the exclusion rules out”.

> **Stacks Project, Tag 0AX9.** A nonzero element of the maximal ideal which, along every
> irreducible component of the special fibre, admits at some closed point of that component and of
> no other a factorization one factor of which lies in the local maximal ideal and restricts to a
> nonzero function on the component.
>
> `hfib` is the standing exclusion of Section 54.7 (Situation 0AX8), transcribed. The section states
> it in these words:
>
> > If $X_s$ has dimension $0$, then $f$ is finite and hence an isomorphism. We will discard this
> > uninteresting case.
>
> So `hfib : 1 ≤ topologicalKrullDim V.specialFiber` is that sentence, and every later lemma of the
> section is read under it. It appears as a binder here only because
> `AlgebraicGeometry.VanishingSituation` transcribes Situation 0AX8 itself, which states the
> situation without the section's subsequent exclusion.
>
> Nothing else is carried. The source passes that exclusion from the fibre to each of its
> components through the geometric connectedness of `X_s`, which it has from the Stein
> factorization — More on Morphisms, Lemma 37.53.6, [Stacks, Tag 0AY8], whose second conclusion is
> not available unconditionally in this library (see
> `StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/NormalBase.lean`, where the
> first conclusion `f_*𝒪_X = 𝒪_S` is tagged and the second is given only over [Stacks, Tag 0G7X]).
> That input is not needed: a zero-dimensional component is a point lying on no other component,
> hence open in the special fibre and so a quasi-finite point of `f`, and a modification of the
> spectrum of a normal local domain with such a point in its closed fibre is an isomorphism
> (`AlgebraicGeometry.IsModification.isIso_of_isOpen_singleton_fiber`), whence the special fibre is
> a single point of dimension zero, which `hfib` forbids. So `hfib` alone gives the observation
> following Situation 54.7.1, that every component has dimension one, as
> `AlgebraicGeometry.VanishingSituation.topologicalKrullDim_component_eq_one`.

```lean
theorem exists_ne_zero_mem_maximalIdeal_factorization_of_le_topologicalKrullDim_specialFiber
    (V : VanishingSituation.{u})
    (hfib : 1 ≤ topologicalKrullDim V.specialFiber) :
    ∃ a : V.A, a ≠ 0 ∧ a ∈ V.maximalIdeal ∧
      ∀ i : Fin V.numberOfComponents,
        ∃ y : componentScheme V i,
          IsClosed
              ({(Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y} : Set V.X) ∧
          (Scheme.IdealSheafData.vanishingIdeal
              (componentClosed V i)).subschemeι y ∈ componentInSource V i ∧
          (∀ j : Fin V.numberOfComponents, j ≠ i →
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y ∉ componentInSource V j) ∧
          ∃ g h : V.X.presheaf.stalk
              ((Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι y),
            g ∈ IsLocalRing.maximalIdeal _ ∧
            (Scheme.IdealSheafData.vanishingIdeal
                (componentClosed V i)).subschemeι.stalkMap y g ≠ 0 ∧
            ((StructureSheaf.toStalk V.A (V.f _) ≫ V.f.stalkMap _) a = g * h)
```

## Tag 0AXA, a lemma

[Tag 0AXA](https://stacks.math.columbia.edu/tag/0AXA) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.invertibleCurveDegree_conormalOnComponent_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegree.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegree.lean#L345). The attribute's comment: “the degree clause -- positivity of deg(C\_\{Z/X}|\_\{C\_i}) at a component C\_i of the special fibre contained in Z -- granted part (2) of Tag 0B40 as the general hypothesis hpos, and granted the global section of the restricted conormal sheaf whose construction from Lemma 0AX9 is the rest of the source's proof”.

> **Stacks Project, Tag 0AXA**, the degree clause at a component carrying the section the
> source's argument produces.
>
> In Situation 0AX8 with `X` normal, let `Z ⊆ X` be a nonempty effective Cartier divisor
> contained set theoretically in the special fibre, and let `C_i` be a component of the special
> fibre contained in `Z`. If the restriction `𝒞_{Z/X}|_{C_i}` of the conormal sheaf of `Z` has a
> nonzero global section with a zero, then `deg(𝒞_{Z/X}|_{C_i}) > 0`.
>
> The component `C_i`, with its reduced induced structure, is an integral scheme proper over the
> residue field `κ` of the closed point of the base, of dimension one by the standing observation
> following Situation 0AX8 which is `hdim`; the restricted conormal sheaf is invertible because
> `ℐ_Z` is. Part (2) of [Stacks, Tag 0B40] then gives the conclusion, and it is carried as the
> hypothesis `hpos`, the library's `AlgebraicGeometry.VanishingSectionDegreePos`, which is
> quantified over every proper integral scheme of dimension at most one over `κ` and every
> invertible sheaf on it, so it mentions none of `X`, `Z` or `C_i`.
>
> What this does *not* do is produce the section, which in the source is the whole of the
> argument: the function of Lemma 0AX9 raised to a power read off from the valuations of the
> local rings at the generic points of the components, after replacing `Z` by `e_i Z`
> ([Stacks, Tags 02OP, 0AYX]) and using that `Z` is `(S_1)` ([Stacks, Tags 0B3S, 0346, 0B3M]) to
> see that the function is a section of `ℐ_Z`.

```lean
theorem invertibleCurveDegree_conormalOnComponent_pos [IsNormal V.X]
    (hdim : ∀ i : Fin V.numberOfComponents, topologicalKrullDim (V.component i) = 1)
    (I : V.X.IdealSheafData) [Stacks.Divisors.IsEffectiveCartierDivisor I]
    (hne : I.supportSet.Nonempty)
    (hZs : I.supportSet ⊆ Set.range (V.f.fiberι V.closedPoint))
    (hpos : VanishingSectionDegreePos (V.base.residueField V.closedPoint))
    (i : Fin V.numberOfComponents) (hCi : componentInSource V i ⊆ I.supportSet)
    (s : (conormalOnComponent V I i).sections) (hs : s.eval (op ⊤) ≠ 0)
    (hzero : ∃ y : componentScheme V i, y ∉ Stacks.SheafOfModules.nonvanishingLocus
      (X := (componentScheme V i).toRingedSpace) (conormalOnComponent V I i) s) :
    0 < invertibleCurveDegree (V.base.residueField V.closedPoint)
      (componentToSpecResidueField V i)
      (topologicalKrullDim_componentScheme_le_one V hdim i) (conormalOnComponent V I i)
```

**`AlgebraicGeometry.VanishingSituation.not_isTrivial_conormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegree.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegree.lean#L400). The attribute's comment: “the first clause -- the conormal sheaf of Z is not trivial -- derived from the degree clause on a component, under the same two grants as invertibleCurveDegree\_conormalOnComponent\_pos”.

> **Stacks Project, Tag 0AXA**, the non-triviality clause, derived from the degree clause.
>
> If the conormal sheaf of `Z` in `X` were trivial, its restriction to a component `C_i ⊆ Z`
> would be isomorphic to the structure sheaf of `C_i` and so would have degree zero, which
> contradicts the positivity of that degree.

```lean
theorem not_isTrivial_conormalSheaf [IsNormal V.X]
    (hdim : ∀ i : Fin V.numberOfComponents, topologicalKrullDim (V.component i) = 1)
    (I : V.X.IdealSheafData) [Stacks.Divisors.IsEffectiveCartierDivisor I]
    (hne : I.supportSet.Nonempty)
    (hZs : I.supportSet ⊆ Set.range (V.f.fiberι V.closedPoint))
    (hpos : VanishingSectionDegreePos (V.base.residueField V.closedPoint))
    (i : Fin V.numberOfComponents) (hCi : componentInSource V i ⊆ I.supportSet)
    (s : (conormalOnComponent V I i).sections) (hs : s.eval (op ⊤) ≠ 0)
    (hzero : ∃ y : componentScheme V i, y ∉ Stacks.SheafOfModules.nonvanishingLocus
      (X := (componentScheme V i).toRingedSpace) (conormalOnComponent V I i) s) :
    ¬ SheafOfModules.IsTrivial I.subscheme.presheaf I.subscheme.ringCatSheaf.2
      (Stacks.Conormal.conormalSheaf I.subschemeι)
```

**`AlgebraicGeometry.VanishingSituation.exists_subset_invertibleCurveDegree_conormalOnComponent_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean, line 708](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean#L708). The attribute's comment: “the precise clause: in Situation 0AX8 with X normal, for a nonempty effective Cartier divisor Z of X contained set theoretically in the special fibre, there is a component C\_i of the special fibre with C\_i contained in Z and deg(C\_\{Z/X}|\_\{C\_i}) > 0”.

> In Situation [Stacks, Tag 0AX8] let `X` be normal and let `Z ⊆ X` be a nonempty effective
> Cartier divisor contained set theoretically in the special fibre. Then there is a component `C_i`
> of the special fibre with `C_i ⊆ Z` and `deg(𝒞_{Z/X}|_{C_i}) > 0`.
>
> The proof is the source's. Let `a ∈ 𝔪` be the function of [Stacks, Tag 0AX9], with its points
> `x_i ∈ C_i` and factorizations `a = g_i h_i` in `𝒪_{X, x_i}`. The local rings `𝒪_{X, ξ_i}` at the
> generic points are discrete valuation rings; let `e_i` be the valuation of `a` and `d_i` that of
> a local equation of `Z`, and pick `i` with `d_i / e_i` maximal (so `d_i > 0` and `C_i ⊆ Z`).
> Then `a^{d_i}` vanishes at the generic points of `e_i Z`, all of which are generic points of
> components of the special fibre, so it is a global section of `ℐ_{e_i Z}` because `e_i Z` is
> `(S_1)` ([Stacks, Tags 0B3S, 0346, 0B3M]). Its restriction to `C_i` is nonzero, since `a^{d_i}`
> generates `ℐ_{e_i Z}` at `ξ_i`, and vanishes at `x_i` by Krull's principal ideal theorem applied
> to `g_i`; so `deg(𝒞_{e_i Z/X}|_{C_i}) > 0` by part (2) of [Stacks, Tag 0B40], and this degree is
> `e_i · deg(𝒞_{Z/X}|_{C_i})` ([Stacks, Tags 02OP, 0B3P, 0AYX]).

```lean
theorem exists_subset_invertibleCurveDegree_conormalOnComponent_pos [IsNormal V.X]
    (I : V.X.IdealSheafData) [hI : Stacks.Divisors.IsEffectiveCartierDivisor I]
    (hne : I.supportSet.Nonempty)
    (hZs : I.supportSet ⊆ Set.range (V.f.fiberι V.closedPoint)) :
    ∃ i : Fin V.numberOfComponents, componentInSource V i ⊆ I.supportSet ∧
      0 < invertibleCurveDegree (V.base.residueField V.closedPoint)
        (componentToSpecResidueField V i)
        (topologicalKrullDim_componentScheme_le_one_of_isNormal V i)
        (conormalOnComponent V I i)
```

**`AlgebraicGeometry.VanishingSituation.not_isTrivial_conormalSheaf_of_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean, line 759](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/ConormalDegreePositive.lean#L759). The attribute's comment: “the first clause: in Situation 0AX8 with X normal, the conormal sheaf of a nonempty effective Cartier divisor Z of X contained set theoretically in the special fibre is not trivial”.

> In Situation [Stacks, Tag 0AX8] with `X` normal, the conormal sheaf of a nonempty effective
> Cartier divisor `Z ⊆ X` contained set theoretically in the special fibre is not trivial. If it
> were, its restriction to the component `C_i ⊆ Z` provided by
> `exists_subset_invertibleCurveDegree_conormalOnComponent_pos` would be isomorphic to `𝒪_{C_i}`
> and so would have degree zero.

```lean
theorem not_isTrivial_conormalSheaf_of_nonempty [IsNormal V.X] (I : V.X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor I] (hne : I.supportSet.Nonempty)
    (hZs : I.supportSet ⊆ Set.range (V.f.fiberι V.closedPoint)) :
    ¬ SheafOfModules.IsTrivial I.subscheme.presheaf I.subscheme.ringCatSheaf.2
      (Stacks.Conormal.conormalSheaf I.subschemeι)
```

## Tag 0AXB, a lemma

[Tag 0AXB](https://stacks.math.columbia.edu/tag/0AXB) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.hOne_restrict_puncturedSpectrum_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/PuncturedBaseCohomology.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/PuncturedBaseCohomology.lean#L256). The attribute's comment: “injectivity, granted the geometric construction of the source's proof as the hypothesis hgeom -- the extension of Tag 0B3A attached to the difference of the two classes, its projective bundle with the section of Tag 0B3V, the second section over f^\{-1}(U) and the scheme-theoretic image of that section, the normalization of the image (finite because A is Nagata, Tags 035S and 035B) and the pullback to it of the first section as a nonempty effective Cartier divisor in the special fibre with trivial conormal sheaf, together with the three inputs that this library's form of Tag 0AXA consumes: the dimension-one observation following Situation 0AX8, part (2) of Tag 0B40 as VanishingSectionDegreePos, and the global section of the restricted conormal sheaf. The contradiction with Tag 0AXA is what is proved here”.

> **Stacks Project, Tag 0AXB.** In Situation 0AX8 with `X` normal and `A` Nagata, the
> restriction map `H¹(X, 𝒪_X) ⟶ H¹(f⁻¹(U), 𝒪_X)` on the first cohomology of the structure sheaf is
> injective.
>
> Two distinct classes with the same restriction are fed to the construction of the source's
> proof, the hypothesis `hgeom`, which returns a nonempty effective Cartier divisor with trivial
> conormal sheaf inside the special fibre of a normal modification of the base; and
> `VanishingSituation.not_isTrivial_conormalSheaf`, which is [Stacks, Tag 0AXA], forbids such a
> divisor.

```lean
theorem hOne_restrict_puncturedSpectrum_injective [IsNormal V.X] (hA : IsNagataRing V.A)
    (hgeom : V.TrivialConormalDivisorOfEqualRestriction) :
    Function.Injective V.firstCohomologyRestriction
```

Declarations registered for the tag:

- [`AlgebraicGeometry.VanishingSituation.firstCohomologyRestriction_injective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/LipDPuncturedRestriction.lean#L478), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/PuncturedRestrictionInjectiveTag.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/PuncturedRestrictionInjectiveTag.lean#L28) (StacksFrontier): “in Situation 0AX8 with X normal, the restriction map H^1(X, O\_X) -> H^1(f^\{-1}(U), O\_X) is injective, for every A (Nagata or not)”.

## Tag 0AXC, a lemma

[Tag 0AXC](https://stacks.math.columbia.edu/tag/0AXC) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.hom_residueFieldShift_derivedPushforwardStructureSheaf_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardAffineIdentification.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardAffineIdentification.lean#L129). The attribute's comment: “the vanishing of Hom\_\{D(A)}(kappa[-1], Rf\_*O\_X) with Rf\_*O\_X the ACTUAL derived direct image: the restricted unbounded derived direct image quasiCoherentDerivedPushforward applied to the structure sheaf of X in degree zero, an object of D\_QCoh(O\_S), carried into D(A) by the inverse of the derived sheafification equivalence of Tag 06Z0 (DualizingDivisor.tildeEquivalence, the affine identification D(A) = D\_QCoh(O\_S) that the tag invokes). The vanishing is the base carrier hom\_residueFieldShift\_derivedGlobalSections\_eq\_zero transported along Leray over the base ring (Tag 0D5W, DualizingDivisor.lerayIso), which identifies that object with the A-linear derived global sections RGamma(X, O\_X). Stated for X normal without the Nagata hypothesis on A, which enters the source's proof only through Tag 0AXB and is not needed on the route taken here”.

> In Situation [Stacks, Tag 0AX8] with `X` normal, the group
> `Hom_{D(A)}(κ[-1], Rf_*𝒪_X)` is zero: every morphism from `κ[-1]` to the derived direct image of
> the structure sheaf, read in `D(A)` through the affine identification `D(A) = D_QCoh(𝒪_S)` of
> [Stacks, Tag 06Z0], vanishes.
>
> Leray over the base ring identifies that object with `RΓ(X, 𝒪_X)`, so this is
> `hom_residueFieldShift_derivedGlobalSections_eq_zero` transported along
> `derivedGlobalSectionsStructureSheafIsoPushforward`. The source also assumes `A` Nagata; that
> hypothesis is not needed, since it enters the source's proof only through
> [Stacks, Tag 0AXB].

```lean
theorem hom_residueFieldShift_derivedPushforwardStructureSheaf_eq_zero [IsNormal V.X]
    (α : V.residueFieldShift ⟶ V.derivedPushforwardStructureSheaf) : α = 0
```

**`AlgebraicGeometry.VanishingSituation.hom_residueFieldShift_derivedGlobalSections_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardStructureSheaf.lean, line 575](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/DerivedPushforwardStructureSheaf.lean#L575). The attribute's comment: “the vanishing of Hom\_\{D(A)}(kappa[-1], Rf\_*O\_X), the pushforward being the derived global sections RGamma(X, O\_X), which isDerivedPushforwardStructureSheaf\_derivedGlobalSectionsStructureSheaf identifies with Rf\_*O\_X by its cohomology H^n(X, O\_X); stated for X normal without the Nagata hypothesis on A, which is not needed. For a nonzero a in the maximal ideal the triangle of 0 -> O\_X -> O\_X -> O\_X/aO\_X -> 0 has first morphism a times the identity, so a morphism out of kappa[-1] factors through RGamma(X, O\_X/aO\_X); in degree zero that is a global section of O\_X/aO\_X annihilated by the maximal ideal, hence supported in the special fibre, hence zero by eq\_zero\_of\_res\_preimagePuncturedSpectrum\_eq\_zero (Lipman's argument from Tag 0AX9, used in place of Tag 0AXB), and Hom\_A(m, A) = A over a Noetherian normal local domain of dimension at least two kills the morphism”.

> **Stacks Project, Tag 0AXC.** In Situation [Stacks, Tag 0AX8] with `X` normal, every
> morphism `κ[-1] ⟶ RΓ(X, 𝒪_X)` in `D(A)` is zero; that is, the group `Hom_{D(A)}(κ[-1], Rf_*𝒪_X)`
> vanishes, the pushforward being read as the derived global sections `RΓ(X, 𝒪_X)`, which
> `isDerivedPushforwardStructureSheaf_derivedGlobalSectionsStructureSheaf` identifies with
> `Rf_*𝒪_X` by its cohomology. The source also assumes `A` Nagata; that is not needed here.
>
> For a nonzero `a ∈ 𝔪` the triangle of `0 → 𝒪_X → 𝒪_X → 𝒪_X/a𝒪_X → 0` has `a • 𝟙` as its first
> morphism, so `α` factors through `RΓ(X, 𝒪_X/a𝒪_X)`. In degree zero the factorisation is a global
> section of `𝒪_X/a𝒪_X` annihilated by `𝔪`. Such a section dies over the punctured spectrum, so it
> is zero by `eq_zero_of_res_preimagePuncturedSpectrum_eq_zero`, and in particular it is the image
> of a global function of `X`. Two consecutive morphisms of the triangle then kill the restriction
> of `α` along `A[-1] ⟶ κ[-1]`, and `Hom_A(𝔪, A) = A` kills `α`.
>
> The source reaches the same lift through [Stacks, Tag 0AXB], whose proof needs the Nagata
> condition to make a normalization finite. Here it comes from the vanishing of sections of
> `𝒪_X/a𝒪_X` supported in the special fibre, which is proved directly by Lipman's argument from
> [Stacks, Tag 0AX9], algebraic Hartogs and the fact that a proper integral curve has no nonconstant
> functions.

```lean
theorem hom_residueFieldShift_derivedGlobalSections_eq_zero (V : VanishingSituation.{u})
    [IsNormal V.X]
    (α : V.residueFieldShift ⟶ derivedGlobalSectionsStructureSheaf V.f) : α = 0
```

## Tag 0B4R, a remark

[Tag 0B4R](https://stacks.math.columbia.edu/tag/0B4R) in the Stacks Project.

**`Stacks.Duality.IsDualizingModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean#L52). The attribute's comment: “dualizing\_module\_terminology”.

> A sheaf of modules on a locally Noetherian scheme is a **dualizing module** when it is
> coherent and becomes a dualizing complex once placed in some cohomological degree.

```lean
abbrev IsDualizingModule {X : Scheme.{u}} [IsLocallyNoetherian X] (ω : X.Modules) : Prop
```

**`Stacks.Duality.IsDualizingRingModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DualizingModule.lean#L59). The attribute's comment: “dualizing\_module\_terminology”.

> A module over a Noetherian ring is a **dualizing module** when it is finite and becomes a
> dualizing complex once placed in some cohomological degree.

```lean
abbrev IsDualizingRingModule (A : Type u) [CommRing A] [IsNoetherianRing A] (M : Type v)
    [AddCommGroup M] [Module A M] : Prop
```

**`Stacks.Duality.exists_isDualizingComplex_iff_exists_isDualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleExistence.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleExistence.lean#L60). The attribute's comment: “the equivalence of (1) and (2)”.

> **Stacks Project, Remark 0B4R, the equivalence of (1) and (2).** An integral Noetherian
> normal scheme of dimension at most two carries a dualizing complex if and only if it carries a
> dualizing module, that is a coherent module which is a dualizing complex in some degree.

```lean
public theorem exists_isDualizingComplex_iff_exists_isDualizingModule (X : Scheme.{u})
    [IsIntegral X] [IsNoetherian X] [IsNormal X] (hX : topologicalKrullDim X ≤ 2) :
    (∃ K : DerivedCategory X.Modules, IsDualizingComplex K) ↔
      ∃ ω : X.Modules, IsDualizingModule ω
```

## Tag 0AXD, a proposition

[Tag 0AXD](https://stacks.math.columbia.edu/tag/0AXD) in the Stacks Project.

**`AlgebraicGeometry.VanishingSituation.isZero_firstCohomology_dualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/GrauertRiemenschneider.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/GrauertRiemenschneider.lean#L194). The attribute's comment: “the conclusion R^1 f\_* omega\_X = 0 read over the affine base S = Spec(A) as the vanishing of H^1(X, omega\_X) as an A-module (Tag 01XJ), granted two inputs of the source's proof as named hypotheses: hfin, the finiteness of H^1(X, omega\_X) over A, which is coherence of the higher direct image of a coherent module under a proper morphism (Tag 02O5) and is used by the source where it produces a nonzero map R^1 f\_* omega\_X -> kappa; and hvanish, the source's duality step, in which RHom\_A(-, omega\_A^bullet) carries a nonzero alpha : Rf\_* omega\_X^bullet -> kappa[1] to a nonzero beta : kappa[-1] -> Rf\_* O\_X and contradicts Tag 0AXC, using RHom\_A(kappa[1], omega\_A^bullet) = kappa[-1] for a normalized omega\_A^bullet (Tag 0A7M), RHom\_A(Rf\_* omega\_X^bullet, omega\_A^bullet) = Rf\_* O\_X (Tags 0GEW, 0AA3) and omega\_X^bullet = omega\_X[2] (Tags 0B3D, 0AWT, 0AWI), carried as the vanishing of every A-linear map H^1(X, omega\_X) -> kappa, which also subsumes the source's normalization of omega\_X with respect to omega\_A (Tag 0B4R), not expressible without f^!; what is proved is the passage from those two to the conclusion, by Nakayama”.

> **Stacks Project, Tag 0AXD** (Grauert-Riemenschneider). In the vanishing situation of
> [Stacks, Tag 0AX8] with `X` normal and `A` Nagata carrying a dualizing complex `ω_A^•`, the
> first cohomology of the dualizing module `ω_X` of `X` vanishes; over the affine base
> `S = Spec(A)` this is `R¹f_*ω_X = 0`.
>
> The two hypotheses carried from the source's proof are `hfin`, the finiteness of `H¹(X, ω_X)`
> over `A`, which comes from coherence of the higher direct images under the proper morphism `f`
> ([Stacks, Tag 02O5]) and is what lets a nonzero module be detected by a map to `κ`; and
> `hvanish`, the outcome of the source's duality step, in which a nonzero `R¹f_*ω_X → κ` is
> dualized by `RHom_A(-, ω_A^•)` into a nonzero `κ[-1] → Rf_*𝒪_X` and contradicts
> [Stacks, Tag 0AXC]. The normalization of `ω_X` with respect to `ω_A` is used by the source only
> inside that step and is subsumed in `hvanish`.

```lean
theorem isZero_firstCohomology_dualizingModule [IsNormal V.X] [IsLocallyNoetherian V.X]
    (hnag : IsNagataRing V.A)
    (ωA : DerivedCategory (ModuleCat.{u} V.A)) (hωA : Dualizing.IsDualizingComplex ωA)
    (ω : V.X.Modules) (hω : Stacks.Duality.IsDualizingModule ω)
    (hfin : Module.Finite V.A (firstCohomologySheafAsBaseModule V.X V.f ω))
    (hvanish : ∀ φ : firstCohomologySheafAsBaseModule V.X V.f ω →ₗ[V.A]
      IsLocalRing.ResidueField V.A, φ = 0) :
    IsZero (firstCohomologySheafAsBaseModule V.X V.f ω)
```

**`AlgebraicGeometry.VanishingSituation.isZero_firstCohomology_normalizedDualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/GrauertRiemenschneiderUnconditional.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/GrauertRiemenschneiderUnconditional.lean#L414). The attribute's comment: “the conclusion R^1 f\_* omega\_X = 0 of Proposition 54.7.8, read over the affine base S = Spec(A) as the vanishing of H^1(X, omega\_X) as an A-module, with no hypothesis beyond the Proposition's own: the Situation of Tag 0AX8, X normal, A Nagata, and A having a dualizing complex in the form of the bare existential. The dualizing module omega\_X of Remark 0B4R is exhibited together with the normalization f^times(omega\_A^bullet-tilde) = omega\_X[2] that singles it out, a dualizing complex being determined only up to shift and twist. The source's proof is carried out in full: omega\_X^bullet = omega\_X[2] (Tags 0B3D, 0AWT, 0AWI), a nonzero R^1 f\_* omega\_X -> kappa gives a nonzero alpha : Rf\_* omega\_X^bullet -> kappa[1], and RHom\_A(-, omega\_A^bullet) carries it to a nonzero beta : kappa[-1] -> Rf\_* O\_X, using RHom\_A(kappa[1], omega\_A^bullet) = kappa[-1] for a normalized omega\_A^bullet (Tag 0A7M) and RHom\_A(Rf\_* omega\_X^bullet, omega\_A^bullet) = Rf\_* O\_X (Tags 0GEW, 0AA3), contradicting Tag 0AXC; Nakayama then gives the vanishing”.

> **Stacks Project, Tag 0AXD** (Grauert-Riemenschneider). Let `(A, 𝔪, κ)` be a
> two-dimensional Noetherian normal local domain, `f : X ⟶ S = Spec(A)` a modification with `X`
> normal, and suppose `A` is Nagata and has a dualizing complex. Then there are a normalized
> dualizing complex `ω_A^•` over `A` and a dualizing module `ω_X` on `X` normalized with respect to
> it — that is, with `f^×(ω̃_A^•) ≅ ω_X[2]`, the dualizing module of [Stacks, Remark 0B4R] — whose
> first cohomology vanishes: `H¹(X, ω_X) = 0`, which over the affine base `S` is `R¹f_*ω_X = 0`.
>
> The dualizing module is exhibited rather than quantified over, because that is what the source's
> `ω_X` is: a dualizing complex on `X` is determined only up to shift and twist by an invertible
> object, and the normalization `f^×(ω̃_A^•) ≅ ω_X[2]` is what picks out the one the statement is
> about.
>
> The proof is the source's, assembled from
> `AlgebraicGeometry.VanishingSituation.isZero_firstCohomology_dualizingModule_of_isTildeDualizing`:
> `ω_A^•` is normalized after one shift ([Stacks, Tag 0A7L] through [Stacks, Tag 0AX1]), its
> derived sheafification is a dualizing complex on `S`
> (`AlgebraicGeometry.VanishingSituation.isDualizingComplex_derivedTilde_base`), and `f^×` of it is
> a coherent module in degree `-2`
> (`AlgebraicGeometry.VanishingSituation.exists_isDualizingModule_properRightAdjoint_isoShiftTwo`),
> which is a dualizing module because `f^×` preserves dualizing complexes ([Stacks, Tag 0AA3]).
>
> **A note on dependency reporting.** A tool that collects axioms from the public oleans can
> report a spurious placeholder dependency for this theorem; this is not a defect of the proof,
> and it affects every declaration in this part of the library.
>
> `Duality/DerivedTilde/AffinePullbackComparison.lean` reaches its key input through `import all`,
> and that input — `CochainComplex.DerivedExtensionScalars.isLeftDerivedFunctor_of_isIso_on_kFlat`
> of `Homology/Tor/DerivedExtensionScalars.lean` — is `private`. A private declaration of another
> module has no entry in Lean's exported-dependency extension and no body in the public olean, so
> such a collector sees only a stub and records a placeholder. Everything above it inherits that
> reading, which is the whole apparent chain through 08DW, 08EU, 0GEW and the duality transport.
> Read in its own module the private lemma is clean, and so is every constant in the statements
> and proofs of the two theorems that consume it.
>
> The proof is complete: no proof in `StacksCore/` or `StacksFrontier/` is left open, Mathlib and every
> dependency are complete, and no elaborator in this repository emits a placeholder. So no library
> declaration can carry one at all.
>
> The spurious report disappears with a three-line change in that one base file: import `Homology/Tor/DerivedChangeOfRings`
> publicly instead of `import all` on `DerivedExtensionScalars`, and call the already-public twin
> `CochainComplex.DerivedTensor.KFlatDerived.isLeftDerivedFunctor_of_isIso_on_kFlat`, which has the
> same signature and whose body lives in its own module. It is mathematically a no-op.

```lean
theorem isZero_firstCohomology_normalizedDualizingModule (V : VanishingSituation.{u})
    [IsNormal V.X]
    (hnag : IsNagataRing V.A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} V.A), Dualizing.IsDualizingComplex K) :
    letI : IsProper V.f := V.modification.isProper
    letI : CompactSpace V.X := QuasiCompact.compactSpace_of_compactSpace V.f
    letI : QuasiSeparatedSpace V.X := quasiSeparatedSpace_of_quasiSeparated V.f
    letI : IsLocallyNoetherian V.X := LocallyOfFiniteType.isLocallyNoetherian V.f
    ∃ (ωA : DerivedCategory (ModuleCat.{u} V.A)) (ωX : V.X.Modules),
      Dualizing.IsNormalizedDualizingComplex.{u, u} ωA ∧ IsDualizingModule ωX ∧
      Nonempty (((properRightAdjoint V.f).obj
          ((derivedTilde (CommRingCat.of V.A)).obj ωA)).obj ≅
        ((DerivedCategory.singleFunctor V.X.Modules 0).obj ωX)⟦(2 : ℤ)⟧) ∧
      IsZero (firstCohomologySheafAsBaseModule V.X V.f ωX)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.7, Tag 0AX7](https://stacks.math.columbia.edu/tag/0AX7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
