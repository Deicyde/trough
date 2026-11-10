---
declaration: section
origin: cited
lean: PrimeSpectrum.isOpen_singleton_tfae_and_exists_algEquiv_prod_of_finiteType, Algebra.isOpen_singleton_fiber_tfae_of_finiteType, quasiFiniteAt_forall_iff_finite_fiber, moduleFinite_fiber_iff_finite_primeSpectrum, quasiFiniteAt_localization_away_iff, four_rings_quasiFiniteAt, RingHom.QuasiFinite.comp, Algebra.quasiFiniteAt_baseChange_iff
statement: formalized
proof: formalized
---

# 10.122 Quasi-finite maps

Section 10.122 of the Stacks Project, [Tag 02MK](https://stacks.math.columbia.edu/tag/02MK). 9 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00PJ, a lemma

[Tag 00PJ](https://stacks.math.columbia.edu/tag/00PJ) in the Stacks Project.

**`PrimeSpectrum.isOpen_singleton_tfae_and_exists_algEquiv_prod_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/FiniteType.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Artinian/FiniteType.lean#L371). The attribute's comment: “The source's field `k` is weakened to an artinian ring; `S_𝔮` is an abstract localization `Sq`, `dim_𝔮 Spec S` is `topologicalKrullDimAt` and `dim S_𝔮` is `𝔮.height`. The closing assertion `S_𝔮 = S_g` is Mathlib's more general `PrimeSpectrum.isLocalization_away_iff_atPrime_of_basicOpen_eq_singleton`, with which this tag is realized jointly. See the module docstring.”. References: EGA 0 (14.1.10), “(1)⇔(4), Spec f.t. alg”; EGA II (6.2.2), “affine, base a field”.

> **Stacks 00PJ.** Let `k` be an artinian ring (a field, in the source), `S` a `k`-algebra of
> finite type, `𝔮` a prime of `S` and `Sq` a model of the local ring `S_𝔮`. The following are
> equivalent: `𝔮` is an isolated point of `Spec S`; `S_𝔮` is finite over `k`; `D(g) = {𝔮}` for some
> `g ∉ 𝔮`; `Spec S` has dimension `0` at `𝔮`; `𝔮` is a closed point and `dim S_𝔮 = 0`; the residue
> field `κ(𝔮)` is finite over `k` and `dim S_𝔮 = 0`. In that case `S = S_𝔮 × S'` for a finite type
> `k`-algebra `S'`, compatibly with the localization map.

```lean
public theorem isOpen_singleton_tfae_and_exists_algEquiv_prod_of_finiteType (k : Type u)
    {S : Type v} [CommRing k] [IsArtinianRing k] [CommRing S] [Algebra k S]
    [Algebra.FiniteType k S] (𝔮 : Ideal S) [𝔮.IsPrime] (Sq : Type w) [CommRing Sq]
    [Algebra S Sq] [IsLocalization.AtPrime Sq 𝔮] [Algebra k Sq] [IsScalarTower k S Sq] :
    List.TFAE
        [IsOpen {(⟨𝔮, ‹_›⟩ : PrimeSpectrum S)},
          Module.Finite k Sq,
          ∃ g ∉ 𝔮, (basicOpen g : Set (PrimeSpectrum S)) = {⟨𝔮, ‹_›⟩},
          topologicalKrullDimAt (PrimeSpectrum S) ⟨𝔮, ‹_›⟩ = 0,
          IsClosed {(⟨𝔮, ‹_›⟩ : PrimeSpectrum S)} ∧ 𝔮.height = 0,
          Module.Finite k 𝔮.ResidueField ∧ 𝔮.height = 0] ∧
      (IsOpen {(⟨𝔮, ‹_›⟩ : PrimeSpectrum S)} →
        ∃ (S' : Type v) (_ : CommRing S') (_ : Algebra k S'), Algebra.FiniteType k S' ∧
          ∃ e : S ≃ₐ[k] Sq × S', ∀ x, (e x).1 = algebraMap S Sq x)
```

## Tag 00PK, a lemma

[Tag 00PK](https://stacks.math.columbia.edu/tag/00PK) in the Stacks Project.

**`Algebra.isOpen_singleton_fiber_tfae_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Basic.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Basic.lean#L492). The attribute's comment: “The fibre is the subspace `comap (algebraMap R S) ⁻¹' {𝔭}` of `Spec S` and `q̄` is `𝔮` itself; `S_𝔮/𝔭S_𝔮` is `κ(𝔭) ⊗_R S_𝔮`, i.e. `𝔭.Fiber (Localization.AtPrime 𝔮)`; `dim_q̄ F` is `topologicalKrullDimAt`. See the module docstring.”. References: EGA 0 (14.1.10), “(1)⇔(4) for fibres”; EGA II (6.2.1), “affine case”; EGA II (6.2.2), “affine case, one prime”.

> **Stacks 00PK.** Let `R → S` be of finite type, let `𝔮` be a prime of `S` lying over a prime
> `𝔭` of `R`, let `F = Spec (S ⊗_R κ(𝔭))` be the fibre of `Spec S → Spec R` over `𝔭` and let `q̄`
> be the point of `F` corresponding to `𝔮`. The following are equivalent: `q̄` is an isolated
> point of `F`; `S_𝔮/𝔭S_𝔮` is finite over `κ(𝔭)`; some `g ∉ 𝔮` has `𝔮` as the only prime of
> `D(g)` lying over `𝔭`; `dim_q̄ F = 0`; `q̄` is a closed point of `F` and `dim S_𝔮/𝔭S_𝔮 = 0`;
> `κ(𝔮)/κ(𝔭)` is finite and `dim S_𝔮/𝔭S_𝔮 = 0`.

```lean
public theorem isOpen_singleton_fiber_tfae_of_finiteType {R S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FiniteType R S] (𝔭 : Ideal R) [𝔭.IsPrime] (𝔮 : Ideal S) [𝔮.IsPrime]
    [𝔮.LiesOver 𝔭] [Algebra (Localization.AtPrime 𝔭) (Localization.AtPrime 𝔮)]
    [Localization.AtPrime.IsLiesOverAlgebra 𝔭 𝔮] :
    List.TFAE
      [IsOpen (X := PrimeSpectrum.comap (algebraMap R S) ⁻¹' {(⟨𝔭, ‹_›⟩ : PrimeSpectrum R)})
          {⟨⟨𝔮, ‹_›⟩, PrimeSpectrum.ext (𝔮.over_def 𝔭).symm⟩},
        Module.Finite 𝔭.ResidueField (𝔭.Fiber (Localization.AtPrime 𝔮)),
        ∃ g ∉ 𝔮, {q ∈ 𝔭.primesOver S | g ∉ q} = {𝔮},
        topologicalKrullDimAt
            ↥(PrimeSpectrum.comap (algebraMap R S) ⁻¹' {(⟨𝔭, ‹_›⟩ : PrimeSpectrum R)})
            ⟨⟨𝔮, ‹_›⟩, PrimeSpectrum.ext (𝔮.over_def 𝔭).symm⟩ = 0,
        IsClosed (X := PrimeSpectrum.comap (algebraMap R S) ⁻¹' {(⟨𝔭, ‹_›⟩ : PrimeSpectrum R)})
            {⟨⟨𝔮, ‹_›⟩, PrimeSpectrum.ext (𝔮.over_def 𝔭).symm⟩} ∧
          ringKrullDim (𝔭.Fiber (Localization.AtPrime 𝔮)) = 0,
        Module.Finite 𝔭.ResidueField 𝔮.ResidueField ∧
          ringKrullDim (𝔭.Fiber (Localization.AtPrime 𝔮)) = 0]
```

## Tag 0H8X, a lemma

[Tag 0H8X](https://stacks.math.columbia.edu/tag/0H8X) in the Stacks Project.

**`quasiFiniteAt_forall_iff_finite_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Basic.lean, line 1020](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Basic.lean#L1020). References: EGA II (6.2.2), “affine case, b)⇔c)”.

> Stacks tag 0H8X, the equivalence of conditions (1) and (2): a finite type ring
> map `R → S` is quasi-finite at every prime of `S` lying over a prime `p` of `R` if
> and only if the fibre `S ⊗_R κ(p)` is a finite `κ(p)`-module.

```lean
theorem quasiFiniteAt_forall_iff_finite_fiber
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] (p : Ideal R) [p.IsPrime] :
    -- (1) quasi-finite at every prime of S lying over p
    (∀ (q : Ideal S) [q.IsPrime], q.comap (algebraMap R S) = p →
        Algebra.QuasiFiniteAt R q)
    -- (2) the fibre S ⊗_R κ(p) is a finite κ(p)-module
    ↔ Module.Finite p.ResidueField (p.Fiber S)
```

**`moduleFinite_fiber_iff_finite_primeSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Basic.lean, line 1060](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Basic.lean#L1060). References: EGA II (6.2.2), “affine, one fibre a)⇔b)”.

> Stacks tag 0H8X, the equivalence of conditions (2) and (3): for a finite type
> ring map `R → S` and a prime `p` of `R`, the fibre `S ⊗_R κ(p)` is a finite
> `κ(p)`-module if and only if its prime spectrum `Spec(S ⊗_R κ(p))` is finite.

```lean
theorem moduleFinite_fiber_iff_finite_primeSpectrum
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] (p : Ideal R) [p.IsPrime] :
    -- (2) the fibre S ⊗_R κ(p) is a finite κ(p)-module
    Module.Finite p.ResidueField (p.Fiber S)
    -- (3) Spec(S ⊗_R κ(p)) is a finite set
    ↔ Finite (PrimeSpectrum (p.Fiber S))
```

## Tag 077H, a lemma

[Tag 077H](https://stacks.math.columbia.edu/tag/077H) in the Stacks Project.

**`quasiFiniteAt_localization_away_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Basic.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Basic.lean#L666).

> Stacks tag 077H (Lemma 10.122.6). For a finite type ring map `R → S`, a prime
> `𝔮 ⊂ S` lying over `𝔭 ⊂ R`, an element `f ∈ R` with `f ∉ 𝔭` and an element
> `g ∈ S` with `g ∉ 𝔮`, with `R_f = Localization.Away f` and
> `S_{fg} = Localization.Away ((algebraMap R S f) * g)` and the induced
> `R_f`-algebra structure on `S_{fg}`, the map `R → S` is quasi-finite at `𝔮` iff
> `R_f → S_{fg}` is quasi-finite at `Q = 𝔮 S_{fg}`.

```lean
theorem quasiFiniteAt_localization_away_iff
    {R S Rf Sfg : Type*}
    [CommRing R] [CommRing S] [CommRing Rf] [CommRing Sfg]
    [Algebra R S] [Algebra R Rf] [Algebra R Sfg] [Algebra S Sfg] [Algebra Rf Sfg]
    [IsScalarTower R S Sfg] [IsScalarTower R Rf Sfg]
    (f : R) (g : S)
    [IsLocalization.Away f Rf]
    [IsLocalization.Away (algebraMap R S f * g) Sfg]
    [Algebra.FiniteType R S]
    (p : Ideal R) (q : Ideal S) [p.IsPrime] [q.IsPrime] [q.LiesOver p]
    (hf : f ∉ p) (hg : g ∉ q)
    (Q : Ideal Sfg) (hQ : Q = Ideal.map (algebraMap S Sfg) q) [Q.IsPrime] :
    Algebra.QuasiFiniteAt R q ↔ Algebra.QuasiFiniteAt Rf Q
```

## Tag 00PN, a lemma

[Tag 00PN](https://stacks.math.columbia.edu/tag/00PN) in the Stacks Project.

**`four_rings_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Basic.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Basic.lean#L543).

> **Four rings lemma.** Given a commutative square of rings
> `R → S`, `R → R'`, `R' → S'`, `S → S'` (encoded by `Algebra` instances and the
> appropriate `IsScalarTower` data) such that `R → S` is of finite type and the
> canonical map `S ⊗_R R' → S'` is surjective, if `R → S` is quasi-finite at the
> prime `q := q'.under S` of `S`, then `R' → S'` is quasi-finite at `q'`.
>
> Proof sketch: base change `R → S` quasi-finite at `q'.under S` along
> `R → R'`, using `Algebra.QuasiFiniteAt.baseChange` with the tensor product
> `R' ⊗[R] S`, to obtain quasi-finiteness of `R' → R' ⊗[R] S` at a suitable
> prime `P` lying over `q'.under S` and below `q'`. Then push along the
> surjective `R'`-algebra map `R' ⊗[R] S →ₐ[R'] S'` using
> `Algebra.QuasiFiniteAt.of_surjectiveOnStalks`.

```lean
theorem four_rings_quasiFiniteAt
    (R S R' S' : Type*)
    [CommRing R] [CommRing S] [CommRing R'] [CommRing S']
    [Algebra R S] [Algebra R R'] [Algebra R' S'] [Algebra R S'] [Algebra S S']
    [IsScalarTower R R' S']
    [IsScalarTower R S S']
    [Algebra.FiniteType R S]
    (hsurj : Function.Surjective
      (Algebra.TensorProduct.productMap
        (IsScalarTower.toAlgHom R S S')
        (IsScalarTower.toAlgHom R R' S')))
    (q' : Ideal S') [q'.IsPrime]
    [Algebra.QuasiFiniteAt R (q'.under S)] :
    Algebra.QuasiFiniteAt R' q'
```

## Tag 00PO, a lemma

[Tag 00PO](https://stacks.math.columbia.edu/tag/00PO) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.QuasiFinite.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.QuasiFinite.comp#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/QuasiFinite/Basic.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Basic.lean#L618) (StacksFrontier).

## Tag 00PP, a lemma

[Tag 00PP](https://stacks.math.columbia.edu/tag/00PP) in the Stacks Project.

**`Algebra.quasiFiniteAt_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/BaseChange.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/BaseChange.lean#L145). The attribute's comment: “(1). The canonical map `Spec(S') → Spec(S)` is `PrimeSpectrum.comap Algebra.TensorProduct.includeRight.toRingHom`, so the source's equality of subsets of `Spec(S')` is this equivalence quantified over `𝔮'`. Quasi-finiteness at a prime (Definition 00PL) is `Algebra.QuasiFiniteAt`, the source's notion under the finite type hypothesis. The `←` direction is `Algebra.QuasiFiniteAt.baseChange`; `→` is the new content. Part (3) is `Algebra.QuasiFinite.baseChange`, tagged 00PP upstream; see the module docstring for part (2).”.

> Let `R → S` be a ring map of finite type, let `R → R'` be any ring map and set
> `S' = R' ⊗[R] S`. Let `𝔮'` be a prime of `S'` and let `𝔮` be its image under the canonical map
> `Spec(S') → Spec(S)`. Then `R' → S'` is quasi-finite at `𝔮'` if and only if `R → S` is
> quasi-finite at `𝔮`; equivalently, the quasi-finite locus of `Spec(S')` is the inverse image of the
> quasi-finite locus of `Spec(S)`.

```lean
public theorem Algebra.quasiFiniteAt_baseChange_iff {R S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FiniteType R S] (R' : Type*) [CommRing R'] [Algebra R R']
    (𝔮 : Ideal S) [𝔮.IsPrime] (𝔮' : Ideal (R' ⊗[R] S)) [𝔮'.IsPrime]
    (h : 𝔮 = 𝔮'.comap Algebra.TensorProduct.includeRight.toRingHom) :
    Algebra.QuasiFiniteAt R' 𝔮' ↔ Algebra.QuasiFiniteAt R 𝔮
```

## Tag 0C6H, a lemma

[Tag 0C6H](https://stacks.math.columbia.edu/tag/0C6H) in the Stacks Project.

**`quasiFiniteAt_of_comp_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Basic.lean, line 822](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Basic.lean#L822).

> Permanence of quasi-finiteness (Stacks tag 0C6H): if the composite of
> `f : A →+* B` and `g : B →+* C` is quasi-finite at a prime `r` of `C`, then `g`
> itself is quasi-finite at `r`.

```lean
theorem quasiFiniteAt_of_comp_quasiFiniteAt
    {A B C : Type*} [CommRing A] [CommRing B] [CommRing C]
    (f : A →+* B) (g : B →+* C)
    (r : Ideal C) [r.IsPrime]
    (h : (g.comp f).QuasiFiniteAt r) :
    g.QuasiFiniteAt r
```

## Tag 02ML, a lemma

[Tag 02ML](https://stacks.math.columbia.edu/tag/02ML) in the Stacks Project.

**`Algebra.exists_localization_away_map_finite_of_mem_minimalPrimes_of_finite_primesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/GenericFiniteness.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/GenericFiniteness.lean#L393). The attribute's comment: “The hypothesis is `(𝔭.primesOver S).Finite`; the localizations are arbitrary models (`IsLocalization.Away`), and `R_g → S_g` is the canonical `IsLocalization.Away.map`, whose finiteness is `RingHom.Finite`. See the module docstring.”.

> **Generic finiteness of a finite-type map with finite fibre over a minimal prime.**
> Let `R → S` be a ring map of finite type, let `𝔭` be a minimal prime of `R`, and assume that only
> finitely many primes of `S` lie over `𝔭`. Then there is a `g ∈ R`, `g ∉ 𝔭`, such that the induced
> map `R_g → S_g` on localizations away from `g` and from its image is finite.

```lean
public theorem Algebra.exists_localization_away_map_finite_of_mem_minimalPrimes_of_finite_primesOver
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S] {𝔭 : Ideal R}
    (h𝔭 : 𝔭 ∈ minimalPrimes R) (hfin : (𝔭.primesOver S).Finite) :
    ∃ g ∉ 𝔭, ∀ (Rg Sg : Type*) [CommRing Rg] [CommRing Sg] [Algebra R Rg] [Algebra S Sg]
      [IsLocalization.Away g Rg] [IsLocalization.Away (algebraMap R S g) Sg],
      (IsLocalization.Away.map Rg Sg (algebraMap R S) g).Finite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.122, Tag 02MK](https://stacks.math.columbia.edu/tag/02MK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
