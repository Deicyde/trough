---
declaration: section
origin: cited
lean: Algebra.IsStandardEtale, StandardEtalePair, StandardEtalePair.equivAwayQuotient, standardEtalePair_isEtale, standardEtalePair_baseChange_isStandardEtale, standardEtalePair_localizationAway, standardEtale_not_isStableUnderComposition, Algebra.exists_etale_liesOver_residueFieldRingEquiv
statement: formalized
proof: formalized
---

# 10.144 Local structure of étale ring maps

Section 10.144 of the Stacks Project, [Tag 0G1A](https://stacks.math.columbia.edu/tag/0G1A). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00UB, a definition

[Tag 00UB](https://stacks.math.columbia.edu/tag/00UB) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.IsStandardEtale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsStandardEtale#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L172) (StacksFrontier): “the property of an `R`-algebra”.
- [`StandardEtalePair`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=StandardEtalePair#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L173) (StacksFrontier): “the pair `(f, g)`”.
- [`StandardEtalePair.equivAwayQuotient`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=StandardEtalePair.equivAwayQuotient#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L174) (StacksFrontier): “its ring, as `R[x]_g/(f)`”.

## Tag 00UC, a lemma

[Tag 00UC](https://stacks.math.columbia.edu/tag/00UC) in the Stacks Project.

**`standardEtalePair_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L240). The attribute's comment: “(1)”. References: EGA IV (18.4.3), “(F)”; SGA 1 I (7.3), “partial”; SGA 1 I (7.4), “partial”.

> For an explicit standard étale pair `(f, g)` over `R`, the canonical map
> `R → R[x]_g/(f)` is étale.

```lean
theorem standardEtalePair_isEtale {R : Type*} [CommRing R] (P : StandardEtalePair R) :
    Algebra.Etale R P.Ring
```

**`standardEtalePair_baseChange_isStandardEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L260). The attribute's comment: “(2)”. References: SGA 1 IX (1.3), “standard étale case”.

> The base change `T ⊗[R] (R[x]_g/(f))` is standard étale over `T`.

```lean
theorem standardEtalePair_baseChange_isStandardEtale {R T : Type*} [CommRing R]
    [CommRing T] [Algebra R T] (P : StandardEtalePair R) :
    Algebra.IsStandardEtale T (T ⊗[R] P.Ring)
```

**`standardEtalePair_localizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L270). The attribute's comment: “(3)”.

> For a standard étale pair `(f, g)` over `R` with ring `A = R[x]_g/(f)` and any `α : A`, the
> composite `R → A → A[1/α]` is standard étale.

```lean
theorem standardEtalePair_localizationAway {R : Type*} [CommRing R]
    (P : StandardEtalePair R) (α : P.Ring)
    (Aα : Type*) [CommRing Aα] [Algebra P.Ring Aα] [Algebra R Aα]
    [IsScalarTower R P.Ring Aα] [IsLocalization.Away α Aα] :
    Algebra.IsStandardEtale R Aα
```

**`standardEtale_not_isStableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L512). The attribute's comment: “(4)”.

> There exist commutative rings `R, S, T` with algebra structures forming a scalar tower
> `R → S → T` such that `R → S` and `S → T` are standard étale but the composite `R → T` is not.

```lean
theorem standardEtale_not_isStableUnderComposition :
    ∃ (R S T : Type) (_ : CommRing R) (_ : CommRing S) (_ : CommRing T)
      (_ : Algebra R S) (_ : Algebra S T) (_ : Algebra R T) (_ : IsScalarTower R S T),
      Algebra.IsStandardEtale R S ∧ Algebra.IsStandardEtale S T ∧
        ¬ Algebra.IsStandardEtale R T
```

## Tag 00UD, a lemma

[Tag 00UD](https://stacks.math.columbia.edu/tag/00UD) in the Stacks Project.

**`Algebra.exists_etale_liesOver_residueFieldRingEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/ResidueFieldExtension.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/ResidueFieldExtension.lean#L428). The attribute's comment: “The isomorphism of extensions `κ(p')/κ(p) ≅ κ(p) ⊂ L` is pinned as a ring isomorphism `e : κ(p') ≃+* L` with `e ∘ Ideal.ResidueField.map p p' (algebraMap R R') = algebraMap κ(p) L`. Only `Algebra.Etale R R'` is asserted, as in the source's statement; that `R'` may be taken standard étale is Proposition 00UE. See the module docstring.”. References: SGA 2 XIV (3.4), “affine case”.

> **Stacks 00UD.** Let `R` be a ring, `p` a prime of `R` and `L/κ(p)` a finite separable field
> extension. Then there are an étale ring map `R → R'` and a prime `p'` of `R'` lying over `p`
> together with an isomorphism `κ(p') ≃ L` of extensions of `κ(p)`, i.e. one carrying the canonical
> map `κ(p) → κ(p')` induced by `R → R'` to the structure map `κ(p) → L`.

```lean
public theorem exists_etale_liesOver_residueFieldRingEquiv {R : Type u} [CommRing R] (p : Ideal R)
    [p.IsPrime] (L : Type v) [Field L] [Algebra p.ResidueField L]
    [Module.Finite p.ResidueField L] [Algebra.IsSeparable p.ResidueField L] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R')
      (p' : Ideal R') (_ : p'.IsPrime) (_ : p'.LiesOver p) (e : p'.ResidueField ≃+* L),
      (e : p'.ResidueField →+* L).comp
        (Ideal.ResidueField.map p p' (algebraMap R R') (p'.over_def p)) =
          algebraMap p.ResidueField L
```

## Tag 00UE, a proposition

[Tag 00UE](https://stacks.math.columbia.edu/tag/00UE) in the Stacks Project.

**`Algebra.exists_isStandardEtale_of_exists_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/StandardEtale.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/StandardEtale.lean#L149). The attribute's comment: “The hypothesis "étale at `q`" is Definition 00U1 verbatim, `∃ g ∉ Q, Algebra.Etale R (Localization.Away g)`, rather than Mathlib's `Algebra.IsEtaleAt`, which is `Algebra.FormallyEtale R S_Q` and agrees with it only for `S` finitely presented over `R`; the source assumes no finiteness on `S`, so this is strictly more general than Mathlib's `Algebra.IsEtaleAt.exists_isStandardEtale` and implies it. `S_g` is `Localization.Away g` with its `R`-algebra structure the composite `R → S → S_g`. See the module docstring.”.

> Let `R → S` be a ring map and `q ⊂ S` a prime. If `R → S` is étale at `q`, that is, if
> `R → S_g` is étale for some `g ∈ S` with `g ∉ q`, then there is a `g ∈ S`, `g ∉ q`,
> such that `R → S_g` is standard étale.

```lean
public theorem Algebra.exists_isStandardEtale_of_exists_etale {R : Type u} {S : Type v}
    [CommRing R] [CommRing S] [Algebra R S] (Q : Ideal S) [Q.IsPrime]
    (hQ : ∃ g ∉ Q, Algebra.Etale R (Localization.Away g)) :
    ∃ g ∉ Q, Algebra.IsStandardEtale R (Localization.Away g)
```

## Tag 00UF, a lemma

[Tag 00UF](https://stacks.math.columbia.edu/tag/00UF) in the Stacks Project.

**`Algebra.IsStandardEtale.exists_finite_faithfullyFlat_forall_exists_comp_eq_comap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FiniteFlatCover.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/FiniteFlatCover.lean#L373). The attribute's comment: “Conditions (1) and (2) are `Module.Finite`, `Algebra.FinitePresentation` and `Module.FaithfullyFlat` over `R`, faithful flatness being flatness plus surjectivity of `Spec(S') → Spec(R)`; `S'_{g'}` is an arbitrary localization of `S'` away from `g'`; lying over a common prime is the equation between contractions, and the factorization is pinned by an equation between the canonical maps `R → S'_{g'}`. See the module docstring.”.

> **Stacks 00UF.** Let `R → S` be a standard étale ring map. Then there is a finite, finitely
> presented, faithfully flat `R`-algebra `S'` — equivalently, `S'` is finite projective over `R` and
> `Spec(S') → Spec(R)` is surjective — such that for every prime `q ⊂ S` and every prime `q' ⊂ S'`
> lying over the same prime of `R` there are `g' ∈ S'`, `g' ∉ q'`, and a factorization of the
> canonical map `R → S'_{g'}` through a ring map `φ : S → S'_{g'}` with `φ⁻¹(q'S'_{g'}) = q`.

```lean
public theorem Algebra.IsStandardEtale.exists_finite_faithfullyFlat_forall_exists_comp_eq_comap_eq
    (R : Type u) [CommRing R] (S : Type v) [CommRing S] [Algebra R S]
    [Algebra.IsStandardEtale R S] :
    ∃ (S' : Type u) (_ : CommRing S') (_ : Algebra R S') (_ : Module.Finite R S')
      (_ : Algebra.FinitePresentation R S') (_ : Module.FaithfullyFlat R S'),
      ∀ (q : Ideal S) (_ : q.IsPrime) (q' : Ideal S') (_ : q'.IsPrime),
        q.under R = q'.under R → ∃ g' ∉ q', ∀ (B : Type w) (_ : CommRing B) (_ : Algebra S' B)
          (_ : IsLocalization.Away g' B), ∃ φ : S →+* B,
            φ.comp (algebraMap R S) = (algebraMap S' B).comp (algebraMap R S') ∧
              (q'.map (algebraMap S' B)).comap φ = q
```

## Tag 00UG, a lemma

[Tag 00UG](https://stacks.math.columbia.edu/tag/00UG) in the Stacks Project.

**`Algebra.Etale.exists_finite_faithfullyFlat_forall_exists_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FiniteFlatCover.lean, line 689](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/FiniteFlatCover.lean#L689). The attribute's comment: “Hypotheses (1) and (2) are `Algebra.Etale` and `Module.FaithfullyFlat` over `R`, faithful flatness being flatness — which étale supplies — plus surjectivity of `Spec(S) → Spec(R)`; conclusions (1) and (2) are likewise `Module.Finite`, `Algebra.FinitePresentation` and `Module.FaithfullyFlat` over `R`. `S'_{g'}` is an arbitrary localization of `S'` away from `g'`, and the factorization in (3) is pinned by an equation between the canonical maps `R → S'_{g'}`. See the module docstring.”.

> **Stacks 00UG.** Let `R → S` be a ring map which is étale and surjective on spectra. Then
> there is a finite, finitely presented, faithfully flat `R`-algebra `S'` — equivalently, `S'` is
> finite projective over `R` and `Spec(S') → Spec(R)` is surjective — such that for every prime
> `q' ⊂ S'` there is a `g' ∈ S'`, `g' ∉ q'`, for which the canonical map `R → S'_{g'}` factors as
> `R → S → S'_{g'}`.

```lean
public theorem Algebra.Etale.exists_finite_faithfullyFlat_forall_exists_comp_eq
    (R : Type u) [CommRing R] (S : Type v) [CommRing S] [Algebra R S]
    [Algebra.Etale R S] [Module.FaithfullyFlat R S] :
    ∃ (S' : Type u) (_ : CommRing S') (_ : Algebra R S') (_ : Module.Finite R S')
      (_ : Algebra.FinitePresentation R S') (_ : Module.FaithfullyFlat R S'),
      ∀ (q' : Ideal S') (_ : q'.IsPrime), ∃ g' ∉ q', ∀ (B : Type w) (_ : CommRing B)
        (_ : Algebra S' B) (_ : IsLocalization.Away g' B), ∃ φ : S →+* B,
          φ.comp (algebraMap R S) = (algebraMap S' B).comp (algebraMap R S')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.144, Tag 0G1A](https://stacks.math.columbia.edu/tag/0G1A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
