---
declaration: section
origin: cited
lean: Stacks.RegularLocalRing.ShortFreeResolution.solution, IsRegularLocalRing.exists_leftResolution_free_finite_and_hasProjectiveDimensionLE, Ring.forall_hasProjectiveDimensionLE_iff_forall_isLocalization_maximal, IsLocalRing.finrank_cotangentSpace_le_projectiveDimension_residueField, Module.projectiveDimension_le_ringKrullDim, isRegularLocalRing_tfae, IsLocalRing.isRegularRing_tfae, IsRegularRing.isRegularLocalRing_of_isLocalization
statement: formalized
proof: formalized
---

# 10.110 Regular rings and global dimension

Section 10.110 of the Stacks Project, [Tag 065U](https://stacks.math.columbia.edu/tag/065U). 9 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00O7, a proposition

[Tag 00O7](https://stacks.math.columbia.edu/tag/00O7) in the Stacks Project.

**`Stacks.RegularLocalRing.ShortFreeResolution.solution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/GlobalDimension.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularLocalRing/GlobalDimension.lean#L219). The attribute's comment: “Stated with `ringKrullDim R ≤ d` and `e ≤ depth_𝔪(M)`; see the module docstring of the statement file.”. References: EGA 0 (17.3.4), “dim.proj ≤ n - prof”; SGA 2 IV (5.3), “partial”; SGA 6 IX (1.5), “partial”.

> **Stacks 00O7.** Let `R` be a regular local ring of dimension at most `d`. Every finite
> `R`-module `M` whose `𝔪`-depth is at least `e` has a resolution `0 → F_{d-e} → ⋯ → F_0 → M → 0`
> by finite free `R`-modules, and every `R`-module has projective dimension at most `d`.

```lean
public theorem solution {R : Type u} [CommRing R] [IsRegularLocalRing R] {d : ℕ}
    (hd : ringKrullDim R ≤ (d : WithBot ℕ∞)) :
    (∀ (M : ModuleCat.{u} R) [Module.Finite R M] (e : ℕ),
        (e : ℕ∞) ≤ Module.depth R (maximalIdeal R) M →
        ∃ F : ObjectProperty.LeftResolution
            (fun N : ModuleCat.{u} R => Module.Free R N ∧ Module.Finite R N) M,
          ∀ i, d - e < i → IsZero (F.complex.X i)) ∧
      ∀ M : ModuleCat.{u} R, HasProjectiveDimensionLE M d
```

**`IsRegularLocalRing.exists_leftResolution_free_finite_and_hasProjectiveDimensionLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/GlobalDimension.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularLocalRing/GlobalDimension.lean#L366). The attribute's comment: “Stated with `ringKrullDim R ≤ d` and `e ≤ depth_𝔪(M)`; the length `d - e` of the resolution is the vanishing of its terms in degrees `> d - e`, and `R` having global dimension `≤ d` is `∀ M, HasProjectiveDimensionLE M d`. See the module docstring.”. References: EGA 0 (17.3.4), “dim.proj ≤ n - prof”; EGA 0 (17.3.1), “Sufficiency, partial”; SGA 2 IV (5.3), “partial”; SGA 6 IX (1.5), “partial”.

> **Stacks 00O7.** Let `R` be a regular local ring of dimension at most `d`. Every finite
> `R`-module `M` whose `𝔪`-depth is at least `e` has a resolution `0 → F_{d-e} → ⋯ → F_0 → M → 0`
> by finite free `R`-modules, and every `R`-module has projective dimension at most `d`; that is,
> `R` has global dimension at most `d`.

```lean
public theorem IsRegularLocalRing.exists_leftResolution_free_finite_and_hasProjectiveDimensionLE
    {R : Type u} [CommRing R] [IsRegularLocalRing R] {d : ℕ}
    (hd : ringKrullDim R ≤ (d : WithBot ℕ∞)) :
    (∀ (M : ModuleCat.{u} R) [Module.Finite R M] (e : ℕ),
        (e : ℕ∞) ≤ Module.depth R (maximalIdeal R) M →
        ∃ F : ObjectProperty.LeftResolution
            (fun N : ModuleCat.{u} R => Module.Free R N ∧ Module.Finite R N) M,
          ∀ i, d - e < i → IsZero (F.complex.X i)) ∧
      ∀ M : ModuleCat.{u} R, HasProjectiveDimensionLE M d
```

## Tag 00O9, a lemma

[Tag 00O9](https://stacks.math.columbia.edu/tag/00O9) in the Stacks Project.

**`Ring.forall_hasProjectiveDimensionLE_iff_forall_isLocalization_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GlobalDimension/Localization.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GlobalDimension/Localization.lean#L289).

> **Global dimension of a Noetherian ring is detected at the maximal ideals.** For a Noetherian
> ring `R` and `n : ℕ`, every `R`-module has projective dimension `≤ n` if and only if, for every
> maximal ideal `𝔪` of `R`, every module over the localization `R_𝔪` has projective dimension `≤ n`.
> Taking `∃ n` on both sides gives the source's statement that `R` has finite global dimension iff
> the global dimensions of the `R_𝔪` are bounded.

```lean
public theorem Ring.forall_hasProjectiveDimensionLE_iff_forall_isLocalization_maximal
    {R : Type u} [CommRing R] [IsNoetherianRing R] (n : ℕ)
    (Rₘ : (𝔪 : Ideal R) → [𝔪.IsMaximal] → Type v)
    [∀ (𝔪 : Ideal R) [𝔪.IsMaximal], CommRing (Rₘ 𝔪)]
    [∀ (𝔪 : Ideal R) [𝔪.IsMaximal], Algebra R (Rₘ 𝔪)]
    [∀ (𝔪 : Ideal R) [𝔪.IsMaximal], IsLocalization.AtPrime (Rₘ 𝔪) 𝔪] :
    (∀ M : ModuleCat.{u} R, HasProjectiveDimensionLE M n) ↔
      ∀ (𝔪 : Ideal R) [𝔪.IsMaximal] (M : ModuleCat.{v} (Rₘ 𝔪)),
        HasProjectiveDimensionLE M n
```

## Tag 00OA, a lemma

[Tag 00OA](https://stacks.math.columbia.edu/tag/00OA) in the Stacks Project.

**`IsLocalRing.finrank_cotangentSpace_le_projectiveDimension_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/EmbeddingDimension.lean, line 765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalRing/EmbeddingDimension.lean#L765). The attribute's comment: “`dim_κ 𝔪/𝔪²` is the `finrank` of `IsLocalRing.CotangentSpace R` over `IsLocalRing.ResidueField R`, and `pd_R κ` is `CategoryTheory.projectiveDimension` of `κ` in `ModuleCat R`, valued in `WithBot ℕ∞`. See the module docstring.”.

> **The projective dimension of the residue field bounds the embedding dimension.** For a
> Noetherian local ring `(R, 𝔪, κ)`, the projective dimension of `κ` as an `R`-module is at least
> `dim_κ 𝔪/𝔪²`, the dimension of the cotangent space of `R`.

```lean
public theorem finrank_cotangentSpace_le_projectiveDimension_residueField
    {R : Type u} [CommRing R] [IsLocalRing R] [IsNoetherianRing R] :
    (Module.finrank (ResidueField R) (CotangentSpace R) : WithBot ℕ∞) ≤
      projectiveDimension (ModuleCat.of R (ResidueField R))
```

## Tag 00OB, a lemma

[Tag 00OB](https://stacks.math.columbia.edu/tag/00OB) in the Stacks Project.

**`Module.projectiveDimension_le_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ProjectiveDimension/KrullDimension.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/ProjectiveDimension/KrullDimension.lean#L187). The attribute's comment: “Stated for an arbitrary finite module `M` rather than only for `κ`, the source's proof using nothing else; `pd_R M` is `Module.projectiveDimension` (Tag 00O4) and finiteness of it is `≠ ⊤`. See the module docstring.”.

> **Finite projective dimension is bounded by the dimension.** Let `(R, 𝔪)` be a Noetherian
> local ring and let `M` be a finite `R`-module of finite projective dimension. Then
> `pd_R M ≤ dim R`. The source states the case `M = κ`, for which the inequality is an equality
> (Proposition 00OC).

```lean
public theorem projectiveDimension_le_ringKrullDim {R : Type u} [CommRing R] [IsNoetherianRing R]
    [IsLocalRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (hM : projectiveDimension R M ≠ ⊤) :
    projectiveDimension R M ≤ ringKrullDim R
```

## Tag 00OC, a proposition

[Tag 00OC](https://stacks.math.columbia.edu/tag/00OC) in the Stacks Project.

**`isRegularLocalRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/GlobalDimension.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularLocalRing/GlobalDimension.lean#L595). The attribute's comment: “Global dimension is the supremum of the projective dimensions of all `R`-modules (Mathlib has no name for it) and "finite" is `≠ ⊤`; `dim_κ 𝔪/𝔪²` is the `finrank` of `IsLocalRing.CotangentSpace R` over `IsLocalRing.ResidueField R`. The source's two "moreover" equalities are items (4) and (5) of the list, each of which implies the other three. See the module docstring.”. References: EGA 0 (17.3.1).

> **Serre's characterisation of regular local rings** (Stacks 00OC). For a Noetherian local
> ring `(R, 𝔪, κ)` the following are equivalent: (1) `κ` has finite projective dimension over `R`;
> (2) `R` has finite global dimension; (3) `R` is a regular local ring; (4) the global dimension of
> `R` is `dim R`; (5) the global dimension of `R` is `dim_κ 𝔪/𝔪²`. Items (4) and (5) are the
> source's final sentence, and together they give `gl dim R = dim R = dim_κ 𝔪/𝔪²`.

```lean
public theorem isRegularLocalRing_tfae {R : Type u} [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] :
    List.TFAE
      [projectiveDimension (ModuleCat.of R (ResidueField R)) ≠ ⊤,
       (⨆ M : ModuleCat.{u} R, projectiveDimension M) ≠ ⊤,
       IsRegularLocalRing R,
       (⨆ M : ModuleCat.{u} R, projectiveDimension M) = ringKrullDim R,
       (⨆ M : ModuleCat.{u} R, projectiveDimension M) =
         (Module.finrank (ResidueField R) (CotangentSpace R) : WithBot ℕ∞)]
```

## Tag 0AFS, a lemma

[Tag 0AFS](https://stacks.math.columbia.edu/tag/0AFS) in the Stacks Project.

**`IsLocalRing.isRegularRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularRing/GlobalDimension.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularRing/GlobalDimension.lean#L625). The attribute's comment: “Both sentences of the source as one `List.TFAE`: (1) ↔ (2) is the equivalence of regularity with finiteness of the global dimension, and (1) → (3) is "`R_𝔭` is a regular local ring for all primes `𝔭`", spelled with Mathlib's `IsRegularRing` (Definition 00OD). Global dimension is the supremum of the projective dimensions of all `R`-modules, Mathlib having no name for it, and "finite" is `≠ ⊤`. See the module docstring.”. References: EGA 0 (17.3.1), “fin. coh. dim ⇔ regular”; EGA 0 (17.3.1), “fin. coh. dim ⇔ regular”.

> **A regular local ring is a regular ring** (Stacks 0AFS). For a Noetherian local ring `R` the
> following are equivalent: (1) `R` is a regular local ring; (2) `R` has finite global dimension;
> (3) `R` is a regular ring, that is, `R_𝔭` is a regular local ring for every prime `𝔭` of `R`.

```lean
public theorem IsLocalRing.isRegularRing_tfae {R : Type u} [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] :
    List.TFAE
      [IsRegularLocalRing R,
       (⨆ M : ModuleCat.{u} R, projectiveDimension M) ≠ ⊤,
       IsRegularRing R]
```

## Tag 00OD, a definition

[Tag 00OD](https://stacks.math.columbia.edu/tag/00OD) in the Stacks Project.

**`IsRegularRing.isRegularLocalRing_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularRing/Defs.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularRing/Defs.lean#L114). The attribute's comment: “Definition 00OD is Mathlib's class `IsRegularRing`, which is the source's sentence verbatim (`IsNoetherianRing R` plus `IsRegularLocalRing (Localization.AtPrime p)` for every prime `p`), so no predicate is redefined here. Its defining field pins the concrete model `Localization.AtPrime p`, while the source says "the localizations `R_𝔭`"; this is the definition in that model-independent form, universe-polymorphic in the localization. See the module docstring.”.

> **A localization of a regular ring at a prime is a regular local ring** (Stacks 00OD). A
> Noetherian ring `R` is *regular* when all of its localizations `R_𝔭` at primes are regular local
> rings; read for an arbitrary model `S` of `R_𝔭`, that is the statement below.

```lean
public theorem IsRegularRing.isRegularLocalRing_of_isLocalization {R : Type u} [CommRing R]
    [IsRegularRing R] (p : Ideal R) [p.IsPrime] (S : Type v) [CommRing S] [Algebra R S]
    [IsLocalization.AtPrime S p] : IsRegularLocalRing S
```

## Tag 00OE, a lemma

[Tag 00OE](https://stacks.math.columbia.edu/tag/00OE) in the Stacks Project.

**`isRegularRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularRing/GlobalDimension.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularRing/GlobalDimension.lean#L440). The attribute's comment: “Stated for a fixed `n : ℕ`: the source re-quantifies `n` existentially in items (3) and (4), but "with equality for at least one `𝔪`" pins it, and `exists_congr` on `n` recovers the source's reading. Global dimension is the supremum of the projective dimensions of all `R`-modules, Mathlib having no name for it; "regular" is `IsRegularRing` (Definition 00OD) and dimensions are `ringKrullDim`. See the module docstring.”.

> **A Noetherian ring has global dimension `n` if and only if it is regular of dimension `n`**
> (Stacks 00OE). For a Noetherian ring `R` and `n : ℕ` the following are equivalent: (1) the global
> dimension of `R` is `n`; (2) `R` is a regular ring and `dim R = n`; (3) every localization `R_𝔪` at
> a maximal ideal is a regular local ring of dimension `≤ n`, with `dim R_𝔪 = n` for at least one
> `𝔪`; (4) the same for the localizations at all primes.

```lean
public theorem isRegularRing_tfae {R : Type u} [CommRing R] [IsNoetherianRing R] (n : ℕ) :
    List.TFAE
      [(⨆ M : ModuleCat.{u} R, projectiveDimension M) = (n : WithBot ℕ∞),
       IsRegularRing R ∧ ringKrullDim R = (n : WithBot ℕ∞),
       (∀ 𝔪 : Ideal R, ∀ _ : 𝔪.IsMaximal, IsRegularLocalRing (Localization.AtPrime 𝔪) ∧
            ringKrullDim (Localization.AtPrime 𝔪) ≤ (n : WithBot ℕ∞)) ∧
         ∃ 𝔪 : Ideal R, ∃ _ : 𝔪.IsMaximal,
           ringKrullDim (Localization.AtPrime 𝔪) = (n : WithBot ℕ∞),
       (∀ 𝔭 : Ideal R, ∀ _ : 𝔭.IsPrime, IsRegularLocalRing (Localization.AtPrime 𝔭) ∧
            ringKrullDim (Localization.AtPrime 𝔭) ≤ (n : WithBot ℕ∞)) ∧
         ∃ 𝔭 : Ideal R, ∃ _ : 𝔭.IsPrime,
           ringKrullDim (Localization.AtPrime 𝔭) = (n : WithBot ℕ∞)]
```

## Tag 00OF, a lemma

[Tag 00OF](https://stacks.math.columbia.edu/tag/00OF) in the Stacks Project.

**`IsRegularLocalRing.of_flat_of_isLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/FlatLocalHom.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularLocalRing/FlatLocalHom.lean#L518). The attribute's comment: “The source's "local Noetherian and regular" for `S` is the single class `IsRegularLocalRing S` (Definition 00KU), which extends `IsLocalRing` and `IsNoetherianRing`; the homomorphism is `algebraMap R S`, flat as `Module.Flat R S` and local as `IsLocalHom (algebraMap R S)`, the hypothesis pair of `Module.FaithfullyFlat.of_flat_of_isLocalHom`. See the module docstring.”. References: SGA 1 I (9.1), “B regular ⇒ A regular”.

> **Regularity descends along a flat local homomorphism** (Stacks 00OF). Let `R → S` be a local
> homomorphism of local Noetherian rings. If it is flat and `S` is regular, then `R` is regular.

```lean
public theorem IsRegularLocalRing.of_flat_of_isLocalHom {R : Type u} (S : Type v) [CommRing R]
    [CommRing S] [IsLocalRing R] [IsNoetherianRing R] [Algebra R S] [Module.Flat R S]
    [IsLocalHom (algebraMap R S)] [IsRegularLocalRing S] : IsRegularLocalRing R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.110, Tag 065U](https://stacks.math.columbia.edu/tag/065U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
