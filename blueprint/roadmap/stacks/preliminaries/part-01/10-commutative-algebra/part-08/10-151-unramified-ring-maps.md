---
declaration: section
origin: cited
lean: Algebra.GUnramified, Algebra.unramified_iff_and_gUnramified_iff, Algebra.unramified_and_gUnramified_properties, Algebra.GUnramified.baseChange, Algebra.GUnramified.comp, Algebra.GUnramified.of_isLocalization_Away, Algebra.Unramified.quotient, Algebra.GUnramified.quotient_of_fg
statement: formalized
proof: formalized
---

# 10.151 Unramified ring maps

Section 10.151 of the Stacks Project, [Tag 00US](https://stacks.math.columbia.edu/tag/00US). 9 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00UT, a definition

[Tag 00UT](https://stacks.math.columbia.edu/tag/00UT) in the Stacks Project.

**`Algebra.GUnramified`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Defs.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Defs.lean#L122). The attribute's comment: “Item (2). `Ω_{S/R} = 0` is `Algebra.FormallyUnramified` (Lemma 00UO, `Algebra.formallyUnramified_iff`), as in Mathlib's `Algebra.Unramified`, `Algebra.Smooth` and `Algebra.Etale`. Item (1) is `Algebra.Unramified`, item (3) is `∃ g ∉ q, Algebra.Unramified R (Localization.Away g)` and item (4) is `∃ g ∉ q, Algebra.GUnramified R (Localization.Away g)`. See the module docstring.”.

> A ring map `R → S` is **G-unramified** if it is of finite presentation and `Ω_{S/R} = 0`
> (Stacks 00UT (2)); the vanishing of the differentials is recorded as formal unramifiedness, which
> is the same condition by Lemma 00UO. This is the notion of EGA; dropping finite presentation to
> finite type gives `Algebra.Unramified`, item (1) of the same definition.

```lean
public class Algebra.GUnramified (R : Type*) [CommRing R] (S : Type*) [CommRing S] [Algebra R S] :
    Prop
```

## Tag 00UU, a lemma

[Tag 00UU](https://stacks.math.columbia.edu/tag/00UU) in the Stacks Project.

**`Algebra.unramified_iff_and_gUnramified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L126). The attribute's comment: “Both equivalences, as one lemma. `Ω_{S/R} = 0` is written out as `Subsingleton Ω[S⁄R]` on the right of each; on the left, `Algebra.Unramified` and `Algebra.GUnramified` (Definition 00UT) are formal unramifiedness together with finite type resp. finite presentation, so the literal reading of the lemma would be structure eta. See the module docstring.”. References: EGA IV (17.3.2), “(ii) unramified”; EGA IV (17.4.2), “affine case: a) ⇔ c)”.

> **Stacks 00UU.** A ring map `R → S` is unramified if and only if it is of finite type and
> `Ω_{S/R} = 0`, and G-unramified if and only if it is of finite presentation and `Ω_{S/R} = 0`.
> Both equivalences come from the identification of the vanishing of `Ω_{S/R}` with formal
> unramifiedness (Lemma 00UO, `Algebra.formallyUnramified_iff`), which is the condition that
> `Algebra.Unramified` and `Algebra.GUnramified` pair with their finiteness conditions.

```lean
public theorem Algebra.unramified_iff_and_gUnramified_iff (R S : Type*) [CommRing R] [CommRing S]
    [Algebra R S] :
    (Algebra.Unramified R S ↔ Algebra.FiniteType R S ∧ Subsingleton Ω[S⁄R]) ∧
      (Algebra.GUnramified R S ↔ Algebra.FinitePresentation R S ∧ Subsingleton Ω[S⁄R])
```

## Tag 00UV, a lemma

[Tag 00UV](https://stacks.math.columbia.edu/tag/00UV) in the Stacks Project.

**`Algebra.unramified_and_gUnramified_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 926](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L926). The attribute's comment: “All thirteen items, both variants of each, as one conjunction in the source's order; item `n` is the `n`-th conjunct and its `(resp. G-unramified)` reading is that conjunct's second component. The conjuncts share the universe variables `u`, `v`, `w`, and each item is exported under its own name; a proof should cite those names. Items (8) and (9) quantify over a prime of the fibre `κ(𝔭) ⊗_R S` rather than over a prime of `S` lying over `𝔭`. See the module docstring.”.

> **Stacks 00UV.** Properties of unramified and G-unramified ring maps: (1) base change,
> (2) composition, (3) a principal localization, (4) a quotient, (5) an étale map, (6)–(9) four
> criteria at a prime in terms of the vanishing of the differentials, (10) descent along a principal
> open cover, (11) unramifiedness at every prime, (12)–(13) descent to a finite type `ℤ`-algebra.
> Each item has a version for `Algebra.Unramified` and one for `Algebra.GUnramified`, the source's
> "resp.", differing only in whether the finiteness condition is finite type or finite
> presentation. Cite the items by the names listed in the module docstring, not by projecting.

```lean
public theorem Algebra.unramified_and_gUnramified_properties :
    -- (1) base change
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (R' : Type w)
        [CommRing R'] [Algebra R R'], (Unramified R S → Unramified R' (R' ⊗[R] S)) ∧
          (GUnramified R S → GUnramified R' (R' ⊗[R] S))) ∧
    -- (2) composition
    (∀ {R : Type u} {S : Type v} {T : Type w} [CommRing R] [CommRing S] [CommRing T] [Algebra R S]
        [Algebra S T] [Algebra R T] [IsScalarTower R S T],
        (Unramified R S → Unramified S T → Unramified R T) ∧
          (GUnramified R S → GUnramified S T → GUnramified R T)) ∧
    -- (3) a principal localization
    (∀ {R : Type u} [CommRing R] (f : R) (Rf : Type v) [CommRing Rf] [Algebra R Rf]
        [IsLocalization.Away f Rf], GUnramified R Rf ∧ Unramified R Rf) ∧
    -- (4) a quotient
    (∀ {R : Type u} [CommRing R] (I : Ideal R),
        Unramified R (R ⧸ I) ∧ (I.FG → GUnramified R (R ⧸ I))) ∧
    -- (5) an étale map
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] [Etale R S],
        GUnramified R S ∧ Unramified R S) ∧
    -- (6) the stalk of the differentials at the prime vanishes
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (q : Ideal S) [q.IsPrime],
        Subsingleton (LocalizedModule q.primeCompl Ω[S⁄R]) →
          (FiniteType R S → ∃ g ∉ q, Unramified R (Localization.Away g)) ∧
            (FinitePresentation R S → ∃ g ∉ q, GUnramified R (Localization.Away g))) ∧
    -- (7) the fibre of the differentials at the prime vanishes
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (q : Ideal S) [q.IsPrime],
        Subsingleton (q.Fiber Ω[S⁄R]) →
          (FiniteType R S → ∃ g ∉ q, Unramified R (Localization.Away g)) ∧
            (FinitePresentation R S → ∃ g ∉ q, GUnramified R (Localization.Away g))) ∧
    -- (8) the stalk of the differentials of the fibre over `𝔭` vanishes
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (p : Ideal R) [p.IsPrime]
        (q : Ideal (p.Fiber S)) [q.IsPrime],
        Subsingleton (LocalizedModule q.primeCompl Ω[p.Fiber S⁄p.ResidueField]) →
          (FiniteType R S → ∃ g : S,
              Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
                Unramified R (Localization.Away g)) ∧
            (FinitePresentation R S → ∃ g : S,
              Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
                GUnramified R (Localization.Away g))) ∧
    -- (9) the fibre at `q` of the differentials of the fibre over `𝔭` vanishes
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (p : Ideal R) [p.IsPrime]
        (q : Ideal (p.Fiber S)) [q.IsPrime],
        Subsingleton (q.Fiber Ω[p.Fiber S⁄p.ResidueField]) →
          (FiniteType R S → ∃ g : S,
              Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
                Unramified R (Localization.Away g)) ∧
            (FinitePresentation R S → ∃ g : S,
              Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
                GUnramified R (Localization.Away g))) ∧
    -- (10) descent along a cover of `Spec S` by principal opens
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (s : Set S),
        Ideal.span s = ⊤ →
        ((∀ g ∈ s, Unramified R (Localization.Away g)) → Unramified R S) ∧
          ((∀ g ∈ s, GUnramified R (Localization.Away g)) → GUnramified R S)) ∧
    -- (11) unramified at every prime
    (∀ {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S],
        ((∀ (q : Ideal S) [q.IsPrime], ∃ g ∉ q, Unramified R (Localization.Away g)) →
            Unramified R S) ∧
          ((∀ (q : Ideal S) [q.IsPrime], ∃ g ∉ q, GUnramified R (Localization.Away g)) →
            GUnramified R S)) ∧
    -- (12) a G-unramified map is a base change of one over a finite type `ℤ`-algebra
    (∀ {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S], GUnramified R S →
        ∃ (R₀ : Subring R) (S₀ : Type u) (_ : CommRing S₀) (_ : Algebra R₀ S₀),
          FiniteType ℤ R₀ ∧ GUnramified R₀ S₀ ∧ Nonempty (S ≃ₐ[R] R ⊗[R₀] S₀)) ∧
    -- (13) an unramified map is a quotient of a base change of one over a finite type `ℤ`-algebra
    (∀ {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S], Unramified R S →
        ∃ (R₀ : Subring R) (S₀ : Type u) (_ : CommRing S₀) (_ : Algebra R₀ S₀)
          (f : (R ⊗[R₀] S₀) →ₐ[R] S),
          FiniteType ℤ R₀ ∧ Unramified R₀ S₀ ∧ Function.Surjective f)
```

**`Algebra.GUnramified.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1005](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1005). The attribute's comment: “Item (1), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`; the `unramified` version is Mathlib's `Algebra.Unramified.baseChange`.”. References: EGA IV (17.3.3), “(iii) unramified, affine”; EGA IV (17.1.3), “(iii) unram., affine”; SGA 1 I (3.5), “(iii), affine case”.

> **The base change of a G-unramified ring map is G-unramified** (Stacks 00UV (1)); item (1) of
> `Algebra.unramified_and_gUnramified_properties`. This is `Algebra.Unramified.baseChange`, whose
> statement is the other half of the item, with finite type replaced by finite presentation.

```lean
public theorem Algebra.GUnramified.baseChange (R : Type u) [CommRing R] (A : Type v) [CommRing A]
    [Algebra R A] (B : Type w) [CommRing B] [Algebra R B] [GUnramified R A] :
    GUnramified B (B ⊗[R] A)
```

**`Algebra.GUnramified.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1018). The attribute's comment: “Item (2), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`; the `unramified` version is Mathlib's `Algebra.Unramified.comp`.”. References: EGA IV (17.3.3), “(ii) unramified, affine”; EGA IV (17.1.3), “(ii) unram., affine”; SGA 1 I (3.5), “(ii), affine case”.

> **The composition of G-unramified ring maps is G-unramified** (Stacks 00UV (2)); item (2) of
> `Algebra.unramified_and_gUnramified_properties`. This is `Algebra.Unramified.comp`, whose statement
> is the other half of the item, with finite type replaced by finite presentation.

```lean
public theorem Algebra.GUnramified.comp (R : Type u) [CommRing R] (A : Type v) [CommRing A]
    [Algebra R A] (B : Type w) [CommRing B] [Algebra R B] [Algebra A B] [IsScalarTower R A B]
    [GUnramified R A] [GUnramified A B] : GUnramified R B
```

**`Algebra.GUnramified.of_isLocalization_Away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1031](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1031). The attribute's comment: “Item (3), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`; the `unramified` version is Mathlib's `Algebra.Unramified.of_isLocalization_Away`.”.

> **A principal localization `R → R_r` is G-unramified** (Stacks 00UV (3)), stated for an
> arbitrary model `A` of `R_r`; item (3) of `Algebra.unramified_and_gUnramified_properties`. This is
> `Algebra.Unramified.of_isLocalization_Away`, whose statement is the other half of the item, with
> finite type replaced by finite presentation.

```lean
public theorem Algebra.GUnramified.of_isLocalization_Away {R : Type u} [CommRing R] {A : Type v}
    [CommRing A] [Algebra R A] (r : R) [IsLocalization.Away r A] : GUnramified R A
```

**`Algebra.Unramified.quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1039](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1039). The attribute's comment: “Item (4), first sentence, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A quotient `R → R ⧸ I` is unramified** (Stacks 00UV (4), first sentence); item (4) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.Unramified.quotient {R : Type u} [CommRing R] (I : Ideal R) :
    Unramified R (R ⧸ I)
```

**`Algebra.GUnramified.quotient_of_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1047](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1047). The attribute's comment: “Item (4), second sentence, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A quotient `R → R ⧸ I` by a finitely generated ideal is G-unramified** (Stacks 00UV (4),
> second sentence); item (4) of `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.GUnramified.quotient_of_fg {R : Type u} [CommRing R] {I : Ideal R}
    (hI : I.FG) : GUnramified R (R ⧸ I)
```

**`Algebra.GUnramified.of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1057](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1057). The attribute's comment: “Item (5), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`; the `unramified` version is Mathlib's `Algebra.Etale.instUnramified`.”.

> **An étale ring map is G-unramified** (Stacks 00UV (5)); item (5) of
> `Algebra.unramified_and_gUnramified_properties`. This is `Algebra.Etale.instUnramified`, whose
> statement is the other half of the item, with finite type replaced by finite presentation.

```lean
public theorem Algebra.GUnramified.of_etale {R : Type u} [CommRing R] {S : Type v} [CommRing S]
    [Algebra R S] [Etale R S] : GUnramified R S
```

**`Algebra.exists_unramified_away_of_subsingleton_localizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1066](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1066). The attribute's comment: “Item (6), the `unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite type ring map whose differentials have vanishing stalk at a prime `q` is unramified
> at `q`** (Stacks 00UV (6)): there is a `g ∉ q` with `R → S_g` unramified. Item (6) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_unramified_away_of_subsingleton_localizedModule {R : Type u}
    [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [FiniteType R S] (q : Ideal S)
    [q.IsPrime] (hq : Subsingleton (LocalizedModule q.primeCompl Ω[S⁄R])) :
    ∃ g ∉ q, Unramified R (Localization.Away g)
```

**`Algebra.exists_gUnramified_away_of_subsingleton_localizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1077](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1077). The attribute's comment: “Item (6), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite presentation ring map whose differentials have vanishing stalk at a prime `q` is
> G-unramified at `q`** (Stacks 00UV (6)): there is a `g ∉ q` with `R → S_g` G-unramified. Item (6)
> of `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_gUnramified_away_of_subsingleton_localizedModule {R : Type u}
    [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [FinitePresentation R S] (q : Ideal S)
    [q.IsPrime] (hq : Subsingleton (LocalizedModule q.primeCompl Ω[S⁄R])) :
    ∃ g ∉ q, GUnramified R (Localization.Away g)
```

**`Algebra.exists_unramified_away_of_subsingleton_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1088](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1088). The attribute's comment: “Item (7), the `unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite type ring map whose differentials have vanishing fibre at a prime `q` is unramified
> at `q`** (Stacks 00UV (7)): there is a `g ∉ q` with `R → S_g` unramified. Item (7) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_unramified_away_of_subsingleton_fiber {R : Type u} [CommRing R]
    {S : Type v} [CommRing S] [Algebra R S] [FiniteType R S] (q : Ideal S) [q.IsPrime]
    (hq : Subsingleton (q.Fiber Ω[S⁄R])) : ∃ g ∉ q, Unramified R (Localization.Away g)
```

**`Algebra.exists_gUnramified_away_of_subsingleton_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1098](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1098). The attribute's comment: “Item (7), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite presentation ring map whose differentials have vanishing fibre at a prime `q` is
> G-unramified at `q`** (Stacks 00UV (7)): there is a `g ∉ q` with `R → S_g` G-unramified. Item (7)
> of `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_gUnramified_away_of_subsingleton_fiber {R : Type u} [CommRing R]
    {S : Type v} [CommRing S] [Algebra R S] [FinitePresentation R S] (q : Ideal S) [q.IsPrime]
    (hq : Subsingleton (q.Fiber Ω[S⁄R])) : ∃ g ∉ q, GUnramified R (Localization.Away g)
```

**`Algebra.exists_unramified_away_of_subsingleton_localizedModule_of_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1109). The attribute's comment: “Item (8), the `unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite type ring map whose fibre over `p` has differentials with vanishing stalk at a prime
> `q` of that fibre is unramified at `q`** (Stacks 00UV (8)): there is a `g` in `S` whose image in
> `κ(p) ⊗_R S` avoids `q` and with `R → S_g` unramified. Item (8) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_unramified_away_of_subsingleton_localizedModule_of_fiber
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [FiniteType R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal (p.Fiber S)) [q.IsPrime]
    (hq : Subsingleton (LocalizedModule q.primeCompl Ω[p.Fiber S⁄p.ResidueField])) :
    ∃ g : S, Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
      Unramified R (Localization.Away g)
```

**`Algebra.exists_gUnramified_away_of_subsingleton_localizedModule_of_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1123). The attribute's comment: “Item (8), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite presentation ring map whose fibre over `p` has differentials with vanishing stalk at
> a prime `q` of that fibre is G-unramified at `q`** (Stacks 00UV (8)): there is a `g` in `S` whose
> image in `κ(p) ⊗_R S` avoids `q` and with `R → S_g` G-unramified. Item (8) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_gUnramified_away_of_subsingleton_localizedModule_of_fiber
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [FinitePresentation R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal (p.Fiber S)) [q.IsPrime]
    (hq : Subsingleton (LocalizedModule q.primeCompl Ω[p.Fiber S⁄p.ResidueField])) :
    ∃ g : S, Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
      GUnramified R (Localization.Away g)
```

**`Algebra.exists_unramified_away_of_subsingleton_fiber_of_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1137). The attribute's comment: “Item (9), the `unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite type ring map whose fibre over `p` has differentials with vanishing fibre at a prime
> `q` of that fibre is unramified at `q`** (Stacks 00UV (9)): there is a `g` in `S` whose image in
> `κ(p) ⊗_R S` avoids `q` and with `R → S_g` unramified. Item (9) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_unramified_away_of_subsingleton_fiber_of_fiber {R : Type u}
    [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [FiniteType R S] (p : Ideal R)
    [p.IsPrime] (q : Ideal (p.Fiber S)) [q.IsPrime]
    (hq : Subsingleton (q.Fiber Ω[p.Fiber S⁄p.ResidueField])) :
    ∃ g : S, Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
      Unramified R (Localization.Away g)
```

**`Algebra.exists_gUnramified_away_of_subsingleton_fiber_of_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1151). The attribute's comment: “Item (9), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A finite presentation ring map whose fibre over `p` has differentials with vanishing fibre at
> a prime `q` of that fibre is G-unramified at `q`** (Stacks 00UV (9)): there is a `g` in `S` whose
> image in `κ(p) ⊗_R S` avoids `q` and with `R → S_g` G-unramified. Item (9) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.exists_gUnramified_away_of_subsingleton_fiber_of_fiber {R : Type u}
    [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [FinitePresentation R S] (p : Ideal R)
    [p.IsPrime] (q : Ideal (p.Fiber S)) [q.IsPrime]
    (hq : Subsingleton (q.Fiber Ω[p.Fiber S⁄p.ResidueField])) :
    ∃ g : S, Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField) g ∉ q ∧
      GUnramified R (Localization.Away g)
```

**`Algebra.Unramified.of_span_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1164). The attribute's comment: “Item (10), the `unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **Being unramified is local on the target**: if `s ⊆ S` generates the unit ideal and `R → S_g`
> is unramified for every `g ∈ s`, then `R → S` is unramified (Stacks 00UV (10)); item (10) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.Unramified.of_span_eq_top {R : Type u} [CommRing R] {S : Type v}
    [CommRing S] [Algebra R S] {s : Set S} (hs : Ideal.span s = ⊤)
    (H : ∀ g ∈ s, Unramified R (Localization.Away g)) : Unramified R S
```

**`Algebra.GUnramified.of_span_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1174). The attribute's comment: “Item (10), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **Being G-unramified is local on the target**: if `s ⊆ S` generates the unit ideal and
> `R → S_g` is G-unramified for every `g ∈ s`, then `R → S` is G-unramified (Stacks 00UV (10));
> item (10) of `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.GUnramified.of_span_eq_top {R : Type u} [CommRing R] {S : Type v}
    [CommRing S] [Algebra R S] {s : Set S} (hs : Ideal.span s = ⊤)
    (H : ∀ g ∈ s, GUnramified R (Localization.Away g)) : GUnramified R S
```

**`Algebra.Unramified.of_forall_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1183). The attribute's comment: “Item (11), the `unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A ring map unramified at every prime of the target is unramified** (Stacks 00UV (11));
> item (11) of `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.Unramified.of_forall_prime {R : Type u} [CommRing R] {S : Type v}
    [CommRing S] [Algebra R S]
    (H : ∀ (q : Ideal S) [q.IsPrime], ∃ g ∉ q, Unramified R (Localization.Away g)) :
    Unramified R S
```

**`Algebra.GUnramified.of_forall_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1193). The attribute's comment: “Item (11), the `G-unramified` version, exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A ring map G-unramified at every prime of the target is G-unramified** (Stacks 00UV (11));
> item (11) of `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.GUnramified.of_forall_prime {R : Type u} [CommRing R] {S : Type v}
    [CommRing S] [Algebra R S]
    (H : ∀ (q : Ideal S) [q.IsPrime], ∃ g ∉ q, GUnramified R (Localization.Away g)) :
    GUnramified R S
```

**`Algebra.GUnramified.exists_finiteType_int_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1204). The attribute's comment: “Item (12), exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **A G-unramified ring map is a base change of a G-unramified map over a finite type
> `ℤ`-algebra** (Stacks 00UV (12)): there are a subring `R₀ ⊆ R` of finite type over `ℤ` and a
> G-unramified `R₀`-algebra `S₀` with `S ≃ R ⊗_{R₀} S₀` as `R`-algebras. Item (12) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.GUnramified.exists_finiteType_int_baseChange {R : Type u} [CommRing R]
    {S : Type v} [CommRing S] [Algebra R S] [GUnramified R S] :
    ∃ (R₀ : Subring R) (S₀ : Type u) (_ : CommRing S₀) (_ : Algebra R₀ S₀),
      FiniteType ℤ R₀ ∧ GUnramified R₀ S₀ ∧ Nonempty (S ≃ₐ[R] R ⊗[R₀] S₀)
```

**`Algebra.Unramified.exists_finiteType_int_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Properties.lean, line 1215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Properties.lean#L1215). The attribute's comment: “Item (13), exported from `Algebra.unramified_and_gUnramified_properties`.”.

> **An unramified ring map is a quotient of a base change of an unramified map over a finite type
> `ℤ`-algebra** (Stacks 00UV (13)): there are a subring `R₀ ⊆ R` of finite type over `ℤ` and an
> unramified `R₀`-algebra `S₀` with a surjection `R ⊗_{R₀} S₀ → S` of `R`-algebras. Item (13) of
> `Algebra.unramified_and_gUnramified_properties`.

```lean
public theorem Algebra.Unramified.exists_finiteType_int_surjective {R : Type u} [CommRing R]
    {S : Type v} [CommRing S] [Algebra R S] [Unramified R S] :
    ∃ (R₀ : Subring R) (S₀ : Type u) (_ : CommRing S₀) (_ : Algebra R₀ S₀)
      (f : (R ⊗[R₀] S₀) →ₐ[R] S),
      FiniteType ℤ R₀ ∧ Unramified R₀ S₀ ∧ Function.Surjective f
```

## Tag 02FL, a lemma

[Tag 02FL](https://stacks.math.columbia.edu/tag/02FL) in the Stacks Project.

**`exists_isIdempotentElem_isLocalization_away_of_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalStructure.lean, line 849](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalStructure.lean#L849).

> **Stacks Tag 02FL.** If `R → S` is unramified, then there is an idempotent
> `e ∈ S ⊗[R] S` such that the multiplication map `μ : S ⊗[R] S → S` exhibits `S`
> as the localization of `A := S ⊗[R] S` away from `e`. Equivalently (the standard
> reading of "isomorphic as objects under `A`"), the localization map `A → A_e` is
> isomorphic to `μ` under `A`.
>
> Here the `(S ⊗[R] S)`-algebra structure on `S` is the one induced by the
> multiplication map `μ = Algebra.TensorProduct.lmul' R`.

```lean
theorem exists_isIdempotentElem_isLocalization_away_of_unramified (R S : Type*) [CommRing R]
    [CommRing S] [Algebra R S] [Algebra.Unramified R S] :
    ∃ e : S ⊗[R] S, IsIdempotentElem e ∧
      letI : Algebra (S ⊗[R] S) S := (Algebra.TensorProduct.lmul' R).toRingHom.toAlgebra
      IsLocalization.Away e S
```

## Tag 00UW, a lemma

[Tag 00UW](https://stacks.math.columbia.edu/tag/00UW) in the Stacks Project.

**`Algebra.map_eq_maximalIdeal_and_finite_isSeparable_of_unramified_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/ResidueFieldExtension.lean, line 690](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/ResidueFieldExtension.lean#L690). The attribute's comment: “Unramified at `q` is the source's Definition 00UT(3), `∃ g ∉ q, Algebra.Unramified R (Localization.Away g)`. Item (1) is both equalities `p S_q = q S_q` and `q S_q = m_{S_q}`; item (2) is `Module.Finite` and `Algebra.IsSeparable` for `κ(p) → κ(q)`, Mathlib's `Ideal.ResidueField` with the canonical map induced by `R_p → S_q`.”.

> **Stacks 00UW.** Let `R → S` be a ring map and let `q` be a prime of `S` lying over a prime
> `p` of `R`. If `R → S` is unramified at `q` — some `g ∉ q` has `R → S_g` unramified — then
> (1) `p S_q = q S_q`, the maximal ideal of the local ring `S_q`, and (2) the residue field extension
> `κ(q)/κ(p)` is finite separable.

```lean
public theorem Algebra.map_eq_maximalIdeal_and_finite_isSeparable_of_unramified_away
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p]
    [Algebra (Localization.AtPrime p) (Localization.AtPrime q)]
    [Localization.AtPrime.IsLiesOverAlgebra p q]
    (h : ∃ g ∉ q, Algebra.Unramified R (Localization.Away g)) :
    (p.map (algebraMap R (Localization.AtPrime q)) =
        q.map (algebraMap S (Localization.AtPrime q)) ∧
      q.map (algebraMap S (Localization.AtPrime q)) = maximalIdeal (Localization.AtPrime q)) ∧
      Module.Finite p.ResidueField q.ResidueField ∧
      Algebra.IsSeparable p.ResidueField q.ResidueField
```

## Tag 02UR, a lemma

[Tag 02UR](https://stacks.math.columbia.edu/tag/02UR) in the Stacks Project.

**`Algebra.isOpen_singleton_fiber_of_isUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/QuasiFinite.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/QuasiFinite.lean#L195). The attribute's comment: “Unramified at `q` is `Algebra.IsUnramifiedAt R q` (Definition 00UT (3), via `Algebra.exists_unramified_of_isUnramifiedAt`). Quasi-finite at `q` is Definition 00PL, the equivalent conditions of Lemma 00PK, and the conclusion is condition (1), `q` isolated in its fibre; condition (2), `Algebra.QuasiFiniteAt R q`, is instead Mathlib's instance `Algebra.IsUnramifiedAt.instQuasiFiniteOfEssFiniteTypeOfFormallyUnramified`, which holds under weaker hypotheses than the source's. The second sentence needs no declaration: `Algebra.QuasiFinite R S` for `[Algebra.Unramified R S]` is `inferInstance`. See the module docstring.”. References: EGA IV (17.4.3), “affine case”; EGA IV (17.4.1.2), “quasi-finite (ring case)”.

> **Stacks 02UR.** Let `S` be an `R`-algebra of finite type and let `q` be a prime of `S`. If
> `R → S` is unramified at `q` then it is quasi-finite at `q`: the point `q` is isolated in the
> fibre of `Spec S → Spec R` through it. In particular an unramified ring map is quasi-finite: for
> `[Algebra.Unramified R S]`, `Algebra.QuasiFinite R S` is found by instance resolution.

```lean
public theorem Algebra.isOpen_singleton_fiber_of_isUnramifiedAt {R S : Type*} [CommRing R]
    [CommRing S] [Algebra R S] [Algebra.FiniteType R S] (q : PrimeSpectrum S)
    [Algebra.IsUnramifiedAt R q.asIdeal] :
    IsOpen (X := PrimeSpectrum.comap (algebraMap R S) ⁻¹' {q.comap (algebraMap R S)}) {⟨q, rfl⟩}
```

## Tag 02FM, a lemma

[Tag 02FM](https://stacks.math.columbia.edu/tag/02FM) in the Stacks Project.

**`Algebra.exists_unramified_away_of_map_eq_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalRing.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalRing.lean#L57). The attribute's comment: “Unramified at `q` is written as in Definition 00UT (3), as `R → S_g` unramified for some `g ∉ q`, and `κ(q)/κ(p)` is the extension induced by `R_p → S_q`.”.

> **Stacks 02FM.** Let `R → S` be of finite type and let `q` be a prime of `S` lying over the
> prime `p` of `R`. If `p S_q` is the maximal ideal of `S_q` and `κ(q)/κ(p)` is finite separable,
> then `R → S` is unramified at `q`: there is `g ∉ q` such that `R → S_g` is unramified.

```lean
theorem exists_unramified_away_of_map_eq_maximalIdeal {R S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FiniteType R S] (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime]
    [q.LiesOver p] [Algebra (Localization.AtPrime p) (Localization.AtPrime q)]
    [Localization.AtPrime.IsLiesOverAlgebra p q]
    (hmax : p.map (algebraMap R (Localization.AtPrime q)) =
      IsLocalRing.maximalIdeal (Localization.AtPrime q))
    (_hfin : Module.Finite p.ResidueField q.ResidueField)
    (hsep : Algebra.IsSeparable p.ResidueField q.ResidueField) :
    ∃ g ∉ q, Algebra.Unramified R (Localization.Away g)
```

## Tag 08WD, a lemma

[Tag 08WD](https://stacks.math.columbia.edu/tag/08WD) in the Stacks Project.

**`Algebra.Etale.tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L293). The attribute's comment: “The three items are the entries, in the source's order, of one `List.TFAE`. Étale is Mathlib's `Algebra.Etale`, formally étale plus finite presentation, which is the source's Definition 00U1 by its Lemma 00UR; flat is `Module.Flat R S`; G-unramified and unramified are `Algebra.GUnramified` and `Algebra.Unramified` (Definition 00UT). See the module docstring.”.

> **Stacks 08WD.** Let `R → S` be a ring map. The following are equivalent:
>
> 1. `R → S` is étale;
> 2. `R → S` is flat and G-unramified;
> 3. `R → S` is flat, unramified, and of finite presentation.

```lean
public theorem Algebra.Etale.tfae (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] :
    List.TFAE
      [Algebra.Etale R S,
       Module.Flat R S ∧ Algebra.GUnramified R S,
       Module.Flat R S ∧ Algebra.Unramified R S ∧ Algebra.FinitePresentation R S]
```

## Tag 0G1C, a lemma

[Tag 0G1C](https://stacks.math.columbia.edu/tag/0G1C) in the Stacks Project.

**`MvPolynomial.etale_aeval_iff_height_eq_and_span_range_D_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/MvPolynomialCriterion.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/MvPolynomialCriterion.lean#L366). References: SGA 1 II (5.1), “(i) ⟺ (iii)”.

> **Stacks 0G1C.** Let `k` be a field, let `A` be a `k`-algebra of finite type and let
> `a₁, …, aₙ ∈ A`. The `k`-algebra map `φ : k[x₁, …, xₙ] → A`, `xᵢ ↦ aᵢ`, is étale if and only if
> (a) every maximal ideal of `A` has height `n`, equivalently the local rings of `A` at maximal
> ideals have dimension `n`, and (b) the differentials `d(a₁), …, d(aₙ)` generate `Ω[A⁄k]` as an
> `A`-module.

```lean
public theorem MvPolynomial.etale_aeval_iff_height_eq_and_span_range_D_eq_top
    {n : ℕ} (k A : Type*) [Field k] [CommRing A] [Algebra k A] [Algebra.FiniteType k A]
    (a : Fin n → A) :
    (aeval a : MvPolynomial (Fin n) k →ₐ[k] A).toRingHom.Etale ↔
      (∀ m : Ideal A, m.IsMaximal → Ideal.height m = n) ∧
      Submodule.span A (Set.range fun i ↦ KaehlerDifferential.D k A (a i)) = ⊤
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.151, Tag 00US](https://stacks.math.columbia.edu/tag/00US)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
