---
declaration: section
origin: cited
lean: IsLocalRing.exists_flat_residueField_algEquiv, IsLocalRing.exists_finiteEtale_directed_residueField_algEquiv, exists_isFiniteFree_residueField_equiv, Stacks.Flatness.SmallSubalgebras.directedOn_flatSmallSubalgebras, Stacks.Flatness.SmallSubalgebras.sSup_flatSmallSubalgebras, Stacks.Flatness.SmallSubalgebras.faithfullyFlat_of_mem
statement: formalized
proof: formalized
---

# 10.159 Constructing flat ring maps

Section 10.159 of the Stacks Project, [Tag 03C2](https://stacks.math.columbia.edu/tag/03C2). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03C3, a lemma

[Tag 03C3](https://stacks.math.columbia.edu/tag/03C3) in the Stacks Project.

**`IsLocalRing.exists_flat_residueField_algEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FiniteFreeResidueExtension.lean, line 965](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FiniteFreeResidueExtension.lean#L965). The attribute's comment: “The lemma's preamble, a local ring `R'` and a local ring map `R → R'`, is the `Algebra R R'`, `IsLocalRing R'` and `IsLocalHom (algebraMap R R')` binders; the conjuncts are flatness, `𝔪' = 𝔪 R'` as `Ideal.map`, and `k' ≅ K` as an extension of `k` as an `≃ₐ[ResidueField R]`. `K` is allowed to live in a universe of its own, the source's case being `v = u`. See the module docstring.”. References: EGA 0 (10.3.1), “flat local ext, k'≅K”; EGA III (4.3.4), “partial”; SGA 3 V (4.1.2), “first assertion”.

> **A residue field extension is realized by a flat local ring map** (Stacks 03C3). Let
> `(R, 𝔪, k)` be a local ring and let `K` be a field extension of `k`. Then there is a local ring
> `(R', 𝔪', k')` and a local ring map `R → R'` such that `R'` is flat over `R`, `𝔪' = 𝔪 R'`, and
> `k'` is isomorphic to `K` as an extension of `k`.

```lean
theorem IsLocalRing.exists_flat_residueField_algEquiv (R : Type u) [CommRing R]
    [IsLocalRing R] (K : Type v) [Field K] [Algebra (ResidueField R) K] :
    ∃ (R' : Type (max u v)) (_ : CommRing R') (_ : Algebra R R') (_ : IsLocalRing R')
      (_ : IsLocalHom (algebraMap R R')),
      Module.Flat R R' ∧
      (maximalIdeal R).map (algebraMap R R') = maximalIdeal R' ∧
      Nonempty (ResidueField R' ≃ₐ[ResidueField R] K)
```

## Tag 09E0, a lemma

[Tag 09E0](https://stacks.math.columbia.edu/tag/09E0) in the Stacks Project.

**`IsLocalRing.exists_finiteEtale_directed_residueField_algEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/ResidueFieldColimit.lean, line 1111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/ResidueFieldColimit.lean#L1111). The attribute's comment: “The source's directed set `I` and system of finite étale extensions `R ⊂ R_i` with `R' = colim R_i` appear as a directed family `𝒮` of finite étale local `R`-subalgebras of `R'` covering `R'`, which is equivalent since the transition maps of such a system are injective. `K` is allowed to live in a universe of its own, the source's case being `v = u`. See the module docstring.”. References: EGA IV (18.8.6), “(18.8.6.2)”.

> **A separable algebraic residue field extension is realized by a colimit of finite étale
> extensions** (Stacks 09E0). Let `(R, 𝔪, k)` be a local ring and let `K` be a separable algebraic
> extension of `k`. Then there are a local ring `R'`, a local ring map `R → R'`, and a directed
> family `𝒮` of `R`-subalgebras of `R'` whose union is `R'`, each a local ring finite étale over
> `R`, such that the residue field of `R'` is isomorphic to `K` as an extension of `k`.

```lean
public theorem IsLocalRing.exists_finiteEtale_directed_residueField_algEquiv (R : Type u)
    [CommRing R] [IsLocalRing R] (K : Type v) [Field K] [Algebra (ResidueField R) K]
    [Algebra.IsSeparable (ResidueField R) K] :
    ∃ (R' : Type (max u v)) (_ : CommRing R') (_ : Algebra R R') (_ : IsLocalRing R')
      (_ : IsLocalHom (algebraMap R R')) (𝒮 : Set (Subalgebra R R')),
      DirectedOn (· ≤ ·) 𝒮 ∧
      (∀ x : R', ∃ S ∈ 𝒮, x ∈ S) ∧
      (∀ S ∈ 𝒮, Module.Finite R S ∧ Algebra.Etale R S ∧ IsLocalRing S) ∧
      Nonempty (ResidueField R' ≃ₐ[ResidueField R] K)
```

## Tag 07NE, a lemma

[Tag 07NE](https://stacks.math.columbia.edu/tag/07NE) in the Stacks Project.

**`exists_isFiniteFree_residueField_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FiniteFreeResidueExtension.lean, line 651](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FiniteFreeResidueExtension.lean#L651). References: SGA 3 V (4.1.2), “finite K/k case”.

> Stacks Tag 07NE (Lemma 10.159.3). Given a commutative ring `R`, a prime `p`, and a finite
> field extension `L / κ(p)`, there exist a commutative ring `S` and a finite free ring map
> `φ : R →+* S` such that, with `q := pS = Ideal.map φ p`:
> * `q` is prime;
> * `q` lies over `p` (`p = q.comap φ`);
> * the induced residue field extension `κ(q) / κ(p)` is `κ(p)`-isomorphic to `L / κ(p)`, i.e.
>   there is a ring isomorphism `Φ : κ(q) ≃+* L` whose composite with the induced map
>   `κ(p) → κ(q)` equals the structure map `κ(p) → L`.

```lean
theorem exists_isFiniteFree_residueField_equiv.{u, v}
    (R : Type u) [CommRing R] (p : Ideal R) [hp : p.IsPrime]
    (L : Type v) [Field L] [Algebra (ResidueFieldAtPrime R p) L]
    [Module.Finite (ResidueFieldAtPrime R p) L] :
    ∃ (S : Type u) (_ : CommRing S) (φ : R →+* S),
      IsFiniteFree φ ∧
      ∃ (_ : (Ideal.map φ p).IsPrime) (hpq : p = (Ideal.map φ p).comap φ),
        ∃ (Φ : ResidueFieldAtPrime S (Ideal.map φ p) ≃+* L),
          (Φ.toRingHom.comp (inducedResidueMap φ p (Ideal.map φ p) hpq) :
            ResidueFieldAtPrime R p →+* L) = algebraMap (ResidueFieldAtPrime R p) L
```

## Tag 0GIL, a lemma

[Tag 0GIL](https://stacks.math.columbia.edu/tag/0GIL) in the Stacks Project.

**`Stacks.Flatness.SmallSubalgebras.directedOn_flatSmallSubalgebras`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Colimit.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Colimit.lean#L357).

> **(Directedness).** The family `F` of flat `A`-subalgebras of cardinality
> `≤ κ` is directed under inclusion.

```lean
theorem directedOn_flatSmallSubalgebras
    (hB : Module.Flat A B) :
    DirectedOn (· ≤ ·) (flatSmallSubalgebras A B)
```

**`Stacks.Flatness.SmallSubalgebras.sSup_flatSmallSubalgebras`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Colimit.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Colimit.lean#L387).

> **(Covering, supremum form).** The supremum (union) of the family `F` is all
> of `B`.

```lean
theorem sSup_flatSmallSubalgebras
    (hB : Module.Flat A B) :
    sSup (flatSmallSubalgebras A B) = ⊤
```

**`Stacks.Flatness.SmallSubalgebras.faithfullyFlat_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Colimit.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Colimit.lean#L398).

> **(Corollary / remark).** Any member of `F` is faithfully flat over `A`
> whenever `B` is faithfully flat over `A`.

```lean
theorem faithfullyFlat_of_mem
    (hB : Module.FaithfullyFlat A B)
    (B' : Subalgebra A B) (hB' : B' ∈ flatSmallSubalgebras A B) :
    Module.FaithfullyFlat A B'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.159, Tag 03C2](https://stacks.math.columbia.edu/tag/03C2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
