---
declaration: section
origin: cited
lean: filteredColimitEtale_baseChange, CommAlgCat.ind_etale_of_isPushout, isFilteredColimitOfEtaleUnder_of_isColimit, isFilteredColimitOfEtale_colim, CommRingCat.ind_etale_of_comp, CommAlgCat.ind_etale_of_comp, Stacks.Henselian.EtaleLifting.algHom, Stacks.Henselian.EtaleLifting.algHom_spec
statement: formalized
proof: formalized
---

# 10.154 Filtered colimits of étale ring maps

Section 10.154 of the Stacks Project, [Tag 0BSG](https://stacks.math.columbia.edu/tag/0BSG). 7 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BSH, a lemma

[Tag 0BSH](https://stacks.math.columbia.edu/tag/0BSH) in the Stacks Project.

**`filteredColimitEtale_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L635).

> **Stacks 0BSH.** Let `A` and `R'` be commutative `R`-algebras, equivalently ring
> maps `R → A` and `R → R'`. If `A` is a filtered colimit of étale `R`-algebras, then
> `R' ⊗[R] A`, regarded as an `R'`-algebra via the canonical map `R' → R' ⊗[R] A`, is a
> filtered colimit of étale `R'`-algebras. Here `TensorProduct R R' A` is `R' ⊗[R] A`
> with its canonical `R'`-algebra structure.

```lean
theorem filteredColimitEtale_baseChange
    {R : Type u} [CommRing R] {A : Type u} [CommRing A] [Algebra R A]
    {R' : Type u} [CommRing R'] [Algebra R R']
    (hA : IsFilteredColimitOfEtale R A) :
    IsFilteredColimitOfEtale R' (TensorProduct R R' A)
```

**`CommAlgCat.ind_etale_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean, line 1323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L1323). The attribute's comment: “"`Λ` is a filtered colimit of étale `R`-algebras" is `(CommAlgCat.etale R).ind.{u} (CommAlgCat.of R Λ)`, as in Lemma `04GN`, and the source's `S ⊗_R R'` is an abstract `Algebra.IsPushout R S R' S'` rather than a model of the tensor product. Tagged jointly with `filteredColimitEtale_baseChange`, which is this lemma for the predicate `IsFilteredColimitOfEtale` and the model `TensorProduct R R' A`. See the module docstring.”.

> **An ind-étale algebra stays ind-étale after cobase change.** Let `R → S` and `R → R'` be ring
> maps and let `S'` be a pushout of `S` and `R'` over `R`, that is, `S' = S ⊗[R] R'`. If `R'` is a
> filtered colimit of étale `R`-algebras, then `S'` is a filtered colimit of étale `S`-algebras.

```lean
theorem ind_etale_of_isPushout (R S R' S' : Type u) [CommRing R] [CommRing S]
    [CommRing R'] [CommRing S'] [Algebra R S] [Algebra R R'] [Algebra R S'] [Algebra S S']
    [Algebra R' S'] [IsScalarTower R S S'] [IsScalarTower R R' S']
    [Algebra.IsPushout R S R' S']
    (h : (CommAlgCat.etale.{u} R).ind.{u} (CommAlgCat.of R R')) :
    (CommAlgCat.etale.{u} S).ind.{u} (CommAlgCat.of S S')
```

## Tag 0BSJ, a lemma

[Tag 0BSJ](https://stacks.math.columbia.edu/tag/0BSJ) in the Stacks Project.

**`isFilteredColimitOfEtaleUnder_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L407).

> **Stacks 0BSJ.** Let `R` be a commutative ring, let `J` be a small filtered category and let
> `G : J ⥤ Under (CommRingCat.of R)` be a diagram of `R`-algebras with colimit cocone `cA` and
> apex isomorphic to `A`. If every `G.obj j` is a filtered colimit of étale `R`-algebras, then so
> is `A`.

```lean
theorem isFilteredColimitOfEtaleUnder_of_isColimit (R : Type) [CommRing R]
    (A : Under (CommRingCat.of R))
    (J : Type) [SmallCategory J] [IsFiltered J]
    (G : J ⥤ Under (CommRingCat.of R))
    (cA : Limits.Cocone G) (hcA : Limits.IsColimit cA) (hA : cA.pt ≅ A)
    (hEach : ∀ j, IsFilteredColimitOfEtaleUnder R (G.obj j)) :
    IsFilteredColimitOfEtaleUnder R A
```

## Tag 0GIM, a lemma

[Tag 0GIM](https://stacks.math.columbia.edu/tag/0GIM) in the Stacks Project.

**`isFilteredColimitOfEtale_colim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimit/Colimit.lean, line 980](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimit/Colimit.lean#L980).

> **Stacks Tag 0GIM, Lemma 10.154.4.**
>
> Let `I` be a directed set (a nonempty directed preorder). Let `𝓡, 𝓐 : I ⥤ CommRingCat`
> be two functors (the systems `i ↦ R_i` and `i ↦ A_i`) and `α : 𝓡 ⟶ 𝓐` a natural
> transformation (the structure maps `R_i → A_i`, whose naturality squares are the
> required commutative squares with the transition maps).
>
> Take colimits `R = colimit 𝓡` and `A = colimit 𝓐`; the induced structure map
> `R → A` is `colimMap α`. If each `A_i = 𝓐.obj i` is a filtered colimit of étale
> `R_i`-algebras (via the structure map `(α.app i).hom`), then `A` is a filtered
> colimit of étale `R`-algebras (via the induced structure map `(colimMap α).hom`).

```lean
theorem isFilteredColimitOfEtale_colim
    (I : Type u) [Preorder I] [IsDirected I (· ≤ ·)] [Nonempty I]
    (𝓡 𝓐 : I ⥤ CommRingCat.{u}) (α : 𝓡 ⟶ 𝓐)
    (hetale : ∀ i, IsFilteredColimitOfEtaleHom (α.app i).hom) :
    IsFilteredColimitOfEtaleHom (colimMap α).hom
```

## Tag 08HS, a lemma

[Tag 08HS](https://stacks.math.columbia.edu/tag/08HS) in the Stacks Project.

**`CommRingCat.ind_etale_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean, line 754](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L754). The attribute's comment: “"`Λ` is a filtered colimit of étale `R`-algebras" is `ObjectProperty.ind.{u} (fun C : Under R ↦ C.hom.hom.Etale) Λ`, as in Lemma `07C3`; the source's `R`-algebra map `A → B` is a map `g` together with the composite `f ≫ g` as the `R`-algebra structure of `B`, so the triangle commutes by construction. See the module docstring.”.

> **A filtered colimit of étale algebras over a filtered colimit of étale algebras.** Let
> `R → A → B` be ring maps. If `A` and `B` are filtered colimits of étale `R`-algebras, then `B` is
> a filtered colimit of étale `A`-algebras.

```lean
theorem ind_etale_of_comp {R A B : CommRingCat.{u}} (f : R ⟶ A) (g : A ⟶ B)
    (hf : ObjectProperty.ind.{u} (fun C : Under R ↦ C.hom.hom.Etale) (Under.mk f))
    (hfg : ObjectProperty.ind.{u} (fun C : Under R ↦ C.hom.hom.Etale) (Under.mk (f ≫ g))) :
    ObjectProperty.ind.{u} (fun C : Under A ↦ C.hom.hom.Etale) (Under.mk g)
```

**`CommAlgCat.ind_etale_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean, line 1348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L1348). The attribute's comment: “"`Λ` is a filtered colimit of étale `R`-algebras" is `(CommAlgCat.etale R).ind.{u} (CommAlgCat.of R Λ)`, as in Lemma `04GN`, and the source's `A → B → C` is an `IsScalarTower A B C`. Tagged jointly with `CommRingCat.ind_etale_of_comp`, which is this lemma for ring maps and the `ObjectProperty.ind` spelling on `Under R`. See the module docstring.”.

> **A filtered colimit of étale algebras over a filtered colimit of étale algebras.** Let
> `A → B → C` be ring maps. If `B` and `C` are filtered colimits of étale `A`-algebras, then `C` is
> a filtered colimit of étale `B`-algebras.

```lean
theorem ind_etale_of_comp {A B C : Type u} [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hB : (CommAlgCat.etale.{u} A).ind.{u} (CommAlgCat.of A B))
    (hC : (CommAlgCat.etale.{u} A).ind.{u} (CommAlgCat.of A C)) :
    (CommAlgCat.etale.{u} B).ind.{u} (CommAlgCat.of B C)
```

## Tag 08HR, a lemma

[Tag 08HR](https://stacks.math.columbia.edu/tag/08HR) in the Stacks Project.

**`Stacks.Henselian.EtaleLifting.algHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/EtaleLifting/IndEtale.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/EtaleLifting/IndEtale.lean#L665). The attribute's comment: “the map itself; `algHom_spec` is its two defining properties and `algHom_unique` its uniqueness”.

> **The lift of a residue datum along an ind-étale algebra into a henselian local ring**
> (Stacks Tag 08HR, Lemma 10.154.6). Let `R → S` be a ring map with `S` henselian local, let `A` be
> ind-étale over `R`, let `q` be a prime of `A` lying over `p = R ∩ 𝔪 S`, and let
> `τ : κ(q) → κ(S)` be a `κ(p)`-algebra map. This is the `R`-algebra map `A → S` with
> `q = f⁻¹(𝔪 S)` inducing `τ` on residue fields; `algHom_spec` is those two properties and
> `algHom_unique` says it is the only such map.

```lean
noncomputable def algHom
    {R : Type u} {A : Type v} {S : Type w}
    [CommRing R] [CommRing A] [CommRing S] [Algebra R A] [Algebra R S]
    [HenselianLocalRing S]
    (hA : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} A)))
    (p : Ideal R) [p.IsPrime]
    (hp : p = (maximalIdeal S).comap (algebraMap R S))
    (q : Ideal A) [q.IsPrime]
    (hpq : p = q.comap (algebraMap R A))
    (τ : q.ResidueField →+* ResidueField S)
    (hτ : τ.comp (residueFieldMapFib p q hpq) = residueFieldMapBase p hp) :
    A →ₐ[R] S
```

**`Stacks.Henselian.EtaleLifting.algHom_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/EtaleLifting/IndEtale.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/EtaleLifting/IndEtale.lean#L682). The attribute's comment: “the two defining properties of `algHom`”.

> `algHom` pulls the maximal ideal of `S` back to `q` and induces `τ` on residue fields.

```lean
theorem algHom_spec
    {R : Type u} {A : Type v} {S : Type w}
    [CommRing R] [CommRing A] [CommRing S] [Algebra R A] [Algebra R S]
    [HenselianLocalRing S]
    (hA : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} A)))
    (p : Ideal R) [p.IsPrime]
    (hp : p = (maximalIdeal S).comap (algebraMap R S))
    (q : Ideal A) [q.IsPrime]
    (hpq : p = q.comap (algebraMap R A))
    (τ : q.ResidueField →+* ResidueField S)
    (hτ : τ.comp (residueFieldMapFib p q hpq) = residueFieldMapBase p hp) :
    q = (maximalIdeal S).comap (algHom hA p hp q hpq τ hτ : A →+* S) ∧
      InducesResidueMap q (algHom hA p hp q hpq τ hτ : A →+* S) τ
```

**`Stacks.Henselian.EtaleLifting.algHom_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/EtaleLifting/IndEtale.lean, line 733](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/EtaleLifting/IndEtale.lean#L733). The attribute's comment: “uniqueness of `algHom`”.

> `algHom` is the only `R`-algebra map `A → S` pulling `𝔪 S` back to `q` and inducing `τ` on
> residue fields.

```lean
theorem algHom_unique
    {R : Type u} {A : Type v} {S : Type w}
    [CommRing R] [CommRing A] [CommRing S] [Algebra R A] [Algebra R S]
    [HenselianLocalRing S]
    (hA : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} A)))
    (p : Ideal R) [p.IsPrime]
    (hp : p = (maximalIdeal S).comap (algebraMap R S))
    (q : Ideal A) [q.IsPrime]
    (hpq : p = q.comap (algebraMap R A))
    (τ : q.ResidueField →+* ResidueField S)
    (hτ : τ.comp (residueFieldMapFib p q hpq) = residueFieldMapBase p hp)
    (f : A →ₐ[R] S)
    (hf : q = (maximalIdeal S).comap (f : A →+* S) ∧
      InducesResidueMap q (f : A →+* S) τ) :
    f = algHom hA p hp q hpq τ hτ
```

## Tag 08HT, a lemma

[Tag 08HT](https://stacks.math.columbia.edu/tag/08HT) in the Stacks Project.

**`HenselianLocalRing.existsUnique_algEquiv_of_ind_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean, line 1087](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L1087). The attribute's comment: “"`S` is a filtered colimit of étale `R`-algebras" is `(CommAlgCat.etale R).ind (CommAlgCat.of R S)`, as in Lemma 04GN; the source's commutative square is the two `R`-algebra maps to `K`; and "the arrows identify `K` with the residue field" is their surjectivity, `K` being a field. Uniqueness is stated among all `R`-algebra maps `S → S'`, which is stronger than the source's uniqueness among isomorphisms. See the module docstring.”.

> **Uniqueness of the henselization** (Stacks 08HT). Let `R` be a ring, let `S` and `S'` be
> henselian local `R`-algebras that are filtered colimits of étale `R`-algebras, and let
> `p : S →ₐ[R] K` and `p' : S' →ₐ[R] K` be surjections onto a field `K`, so that `K` is the residue
> field of both. Then there is an `R`-algebra isomorphism `e : S ≃ₐ[R] S'` such that an `R`-algebra
> map `f : S → S'` satisfies `p' ∘ f = p` if and only if `f = e`; in particular `e` is the unique
> `R`-algebra isomorphism `S → S'` compatible with the maps to `K`.

```lean
theorem HenselianLocalRing.existsUnique_algEquiv_of_ind_etale
    {R : Type u} [CommRing R] {S S' : Type u} [CommRing S] [CommRing S'] [Algebra R S]
    [Algebra R S'] [HenselianLocalRing S] [HenselianLocalRing S']
    (hS : (CommAlgCat.etale.{u} R).ind.{u} (CommAlgCat.of R S))
    (hS' : (CommAlgCat.etale.{u} R).ind.{u} (CommAlgCat.of R S'))
    {K : Type v} [Field K] [Algebra R K] (p : S →ₐ[R] K) (p' : S' →ₐ[R] K)
    (hp : Function.Surjective p) (hp' : Function.Surjective p') :
    ∃ e : S ≃ₐ[R] S', ∀ f : S →ₐ[R] S', p'.comp f = p ↔ f = (e : S →ₐ[R] S')
```

## Tag 04GI, a lemma

[Tag 04GI](https://stacks.math.columbia.edu/tag/04GI) in the Stacks Project.

**`part2_henselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Colimit.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Colimit.lean#L442). The attribute's comment: “henselian”. References: EGA IV (18.6.14).

> **Part 2 (Henselian case).** If each `R_i` is henselian, then the colimit `R`
> is henselian.
>
> *Argument (Stacks 04GI, the essential new content).* We verify the
> `HenselianLocalRing.is_henselian` clause for `R` (locality is
> `part1_isLocalRing`). Let `g : R[X]` be monic, `a₀ : R` with `g.eval a₀ ∈ m_R`
> and `IsUnit (g.derivative.eval a₀)`; we must find `a : R` with `g.IsRoot a` and
> `a - a₀ ∈ m_R`.
>
> 1. **Descend the data to a finite stage.** Since `R[X]` is the filtered colimit
>    of the `G i[X]`, `Ring.DirectLimit.Polynomial.exists_of` gives an index and a
>    polynomial mapping to `g`; arranging it to be *monic of the same degree*
>    (possible after enlarging the index: the leading coefficient of any preimage
>    maps to `1 = leadingCoeff g`, so `colimit_isUnit_descend`/`of.zero_exact`
>    makes it `1` at a later stage, or one truncates to the correct degree and
>    sets the top coefficient to `1`). Also descend `a₀ = φ_k b₀`
>    (`Ring.DirectLimit.exists_of`). Push polynomial and point to a common index
>    `k`, obtaining a monic `p : G k[X]` with `p.map (φ_k) = g` and `b₀ : G k`
>    with `φ_k b₀ = a₀`.
>
> 2. **The hypotheses descend.** Evaluation commutes with `map`:
>    `φ_k (p.eval b₀) = g.eval a₀` and `φ_k (p.derivative.eval b₀) =
>    g.derivative.eval a₀` (`Polynomial.eval_map`, `Polynomial.derivative_map`).
>    * `g.derivative.eval a₀` is a unit, so `φ_k (p.derivative.eval b₀)` is a unit;
>      by `colimit_isUnit_descend` it becomes a unit `p'.eval ... ` at some `l ≥ k`;
>      push `p, b₀` forward to `l` (so WLOG `k = l`) to get
>      `IsUnit (p.derivative.eval b₀)` in `G k`.
>    * `g.eval a₀ ∈ m_R` means `φ_k (p.eval b₀)` is a nonunit of `R`; if
>      `p.eval b₀` were a unit of `G k`, its image `φ_k (p.eval b₀)` would be a
>      unit of `R` — contradiction. So `p.eval b₀ ∈ m_k`.
>
> 3. **Apply henselianness of `G k`.** `hhens k` gives `c : G k` with
>    `p.IsRoot c` (`p.eval c = 0`) and `c - b₀ ∈ m_k`.
>
> 4. **Push the root forward.** Set `a := φ_k c`. Then
>    `g.eval a = (p.map φ_k).eval (φ_k c) = φ_k (p.eval c) = φ_k 0 = 0`
>    (`Polynomial.eval_map` + `eval₂` is a ring hom), so `g.IsRoot a`. And
>    `a - a₀ = φ_k c - φ_k b₀ = φ_k (c - b₀)`, which lies in `m_R` because
>    `c - b₀ ∈ m_k` and `φ_k` is local (`part1_mem_maximalIdeal` ⟸, or
>    `IsLocalRing.map_nonunit`).

```lean
theorem part2_henselian (hhens : ∀ i, HenselianLocalRing (G i)) :
    HenselianLocalRing (colimitRing G f)
```

**`part3_strictlyHenselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Colimit.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Colimit.lean#L542). The attribute's comment: “strictly henselian”. References: EGA IV (18.8.18), “i)”.

> **Part 3 (Strictly henselian case).** If each `R_i` is strictly henselian
> (henselian with separably closed residue field), then the colimit `R` is strictly
> henselian: it is henselian and its residue field is separably closed.
>
> *Argument.* The henselian conjunct is exactly `part2_henselian G f hlocal hhens`.
> For separable-closedness of `κ_R`: by `part1_residueField_colimit`,
> `κ_R ≃+* colim_i κ_i`, and `IsSepClosed` transports across a ring isomorphism
> (`IsSepClosed` is preserved by `RingEquiv`, e.g. via `RingEquiv.isSepClosed` /
> pulling separable polynomials back and forth). So it suffices that
> `K := colim_i κ_i` is separably closed. Use `IsSepClosed.of_exists_root`: let
> `q : K[X]` be monic, irreducible and separable; we find a root.
> `Ring.DirectLimit.Polynomial.exists_of` descends `q` to `q_i : κ_i[X]` with
> `q_i.map (of i) = q` at some stage `i`; `q` separable forces (after enlarging `i`)
> `q_i` separable and of positive degree. Since `κ_i` is separably closed
> (`hsep i`), `IsSepClosed.exists_root` gives a root `r ∈ κ_i` of `q_i`; its image
> `of i r ∈ K` is a root of `q` (`Polynomial.eval_map`/`eval₂` hom + `of_f`). Hence
> `K` is separably closed, and so is `κ_R`.

```lean
theorem part3_strictlyHenselian
    (hhens : ∀ i, HenselianLocalRing (G i))
    (hsep : ∀ i, IsSepClosed (ResidueField (G i))) :
    letI := part1_isLocalRing G f hlocal
    HenselianLocalRing (colimitRing G f) ∧
      IsSepClosed (ResidueField (colimitRing G f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.154, Tag 0BSG](https://stacks.math.columbia.edu/tag/0BSG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
