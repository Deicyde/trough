---
declaration: section
origin: cited
lean: IsLocalRing.exists_mem_maximalIdeal_bijective_algebraMap_quotient_span_pow, IsLocalRing.exists_finite_faithfullyFlat_forall_isMaximal_isLocalHom_comp_eq
statement: formalized
proof: formalized
---

# 10.146 Local homomorphisms

Section 10.146 of the Stacks Project, [Tag 053J](https://stacks.math.columbia.edu/tag/053J). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GSD, a lemma

[Tag 0GSD](https://stacks.math.columbia.edu/tag/0GSD) in the Stacks Project.

**`IsLocalRing.exists_mem_maximalIdeal_bijective_algebraMap_quotient_span_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/ModuloPowers.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/ModuloPowers.lean#L458). The attribute's comment: “The hypothesis `t ∈ m_R` and the conclusion are the source's; the map shown bijective is the canonical `R/tⁿR → S/tⁿS`. Stated for all `n : ℕ` (the case `n = 0` is the zero ring), with `κ(m_R) → κ(m_S)` merely surjective (equivalent, as it is injective automatically), and with the étale algebra `T` and the prime `q` as hypotheses rather than an existential.”.

> **An étale local homomorphism is an isomorphism modulo powers of a principal ideal.** Let
> `(R, m_R) → (S, m_S)` be a local homomorphism of local rings such that `S` is the localization
> of an étale `R`-algebra `T` at a prime `q`, and such that the residue field extension
> `κ(m_R) → κ(m_S)` is surjective, hence an isomorphism. Then there is `t ∈ m_R` such that
> `R/tⁿR → S/tⁿS` is an isomorphism for every `n`.

```lean
public theorem IsLocalRing.exists_mem_maximalIdeal_bijective_algebraMap_quotient_span_pow
    (R : Type u) [CommRing R] [IsLocalRing R] (S : Type v) [CommRing S] [IsLocalRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)] (T : Type w) [CommRing T] [Algebra R T]
    [Algebra.Etale R T] [Algebra T S] [IsScalarTower R T S] (q : Ideal T) [q.IsPrime]
    [IsLocalization.AtPrime S q]
    (hres : Function.Surjective (IsLocalRing.ResidueField.map (algebraMap R S))) :
    ∃ t ∈ IsLocalRing.maximalIdeal R, ∀ n : ℕ, Function.Bijective
      (algebraMap (R ⧸ Ideal.span {t ^ n}) (S ⧸ (Ideal.span {t ^ n}).map (algebraMap R S)))
```

## Tag 053K, a lemma

[Tag 053K](https://stacks.math.columbia.edu/tag/053K) in the Stacks Project.

**`IsLocalRing.exists_finite_faithfullyFlat_forall_isMaximal_isLocalHom_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/FiniteFlatCover.lean, line 992](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/FiniteFlatCover.lean#L992). The attribute's comment: “The étale algebra `T` and the prime `q` presenting `S` are hypotheses rather than an existential, as in Lemma 0GSD. `R → S'` is `Module.Finite`, `Algebra.FinitePresentation` and `Module.FaithfullyFlat`; `S'_{m'}` is an arbitrary localization of `S'` at `m'`; the factorization is pinned by an equation with the canonical map `R → S'_{m'}`, and the factoring map is required to be local, as in the source's proof. See the module docstring.”.

> **Stacks 053K.** Let `(R, m_R) → (S, m_S)` be a local homomorphism of local rings such that
> `S` is the localization of an étale `R`-algebra `T` at a prime `q`. Then there is a finite,
> finitely presented, faithfully flat `R`-algebra `S'` such that for every maximal ideal `m'` of
> `S'` the canonical map `R → S'_{m'}` factors as `R → S → S'_{m'}`, with `S → S'_{m'}` a local
> homomorphism.

```lean
public theorem IsLocalRing.exists_finite_faithfullyFlat_forall_isMaximal_isLocalHom_comp_eq
    (R : Type u) [CommRing R] [IsLocalRing R] (S : Type v) [CommRing S] [IsLocalRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)] (T : Type w) [CommRing T] [Algebra R T]
    [Algebra.Etale R T] [Algebra T S] [IsScalarTower R T S] (q : Ideal T) [q.IsPrime]
    [IsLocalization.AtPrime S q] :
    ∃ (S' : Type u) (_ : CommRing S') (_ : Algebra R S') (_ : Module.Finite R S')
      (_ : Algebra.FinitePresentation R S') (_ : Module.FaithfullyFlat R S'),
      ∀ (m' : Ideal S') (_ : m'.IsMaximal) (A : Type x) (_ : CommRing A) (_ : Algebra S' A)
        (_ : IsLocalization.AtPrime A m'), ∃ (ψ : S →+* A) (_ : IsLocalHom ψ),
          ψ.comp (algebraMap R S) = (algebraMap S' A).comp (algebraMap R S')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.146, Tag 053J](https://stacks.math.columbia.edu/tag/053J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
