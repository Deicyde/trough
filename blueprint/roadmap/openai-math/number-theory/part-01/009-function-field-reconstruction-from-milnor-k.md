---
declaration: section
origin: cited
lean: OAI.BogomolovPop.main_graph_injective
statement: formalized
proof: formalized
---

# 009. Function-field reconstruction from Milnor K-theory and Galois data

3 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Reconstructs function fields of transcendence degree at least two over algebraically closed constants from $K^{\mathrm M}_1/\ell$, $K^{\mathrm M}_2/\ell$, and their product. These data recover the perfect closure and constants when *ℓ* differs from the characteristic, and the original field and its named base in equal characteristic. Also proves Bogomolov–Pop reconstruction from abelian-by-central pro-*ℓ* Galois data away from the characteristic.

## Reconstruction of Function Fields from Mod-ℓ Milnor K-Theory

We prove a mod-*ℓ* Bogomolov–Pop reconstruction theorem for function fields of transcendence degree at least two over arbitrary algebraically closed fields of characteristic different from *ℓ*. The groups $K^{\mathrm M}_1/\ell$ and $K^{\mathrm M}_2/\ell$, together with their full bilinear product, determine the perfect closure and its constant field. Every compatible isomorphism of these data is induced by a field isomorphism up to a single scalar in $\mathbb F_\ell^\times$, with only Frobenius ambiguity in the field isomorphism in positive characteristic.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf).

## Reconstruction from Milnor K-theory modulo the characteristic

Let *K* and *L* be finitely generated extensions of transcendence degree at least two over algebraically closed fields of characteristic *p*. We prove that every isomorphism of their first Milnor *K*-groups modulo *p* preserving the degree-two Steinberg relations is a nonzero scalar multiple of the map induced by a unique field isomorphism. The proof recovers projective lines over the subfields of *p*th powers by an elementary calculation with derivations.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf).

## The Bogomolov-Pop reconstruction theorem

We prove the Bogomolov–Pop reconstruction conjecture for function fields of transcendence degree at least two over arbitrary algebraically closed fields of characteristic different from *ℓ*. The pro-*ℓ* abelian-by-central datum determines the perfect closure and its constant field, with precisely the Frobenius and *ℓ*-adic unit ambiguities.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Bogomolov–Pop reconstruction conjecture concerns recovering a function field and its constants from pro-$\ell$ abelian-by-central Galois data. The linked formalization proves injectivity of the reconstruction correspondence for function fields of transcendence degree at least two over algebraically closed fields of characteristic different from the prime $\ell$.

If two isomorphisms of perfect closures preserving the constant fields induce the same Galois-data isomorphism modulo $\ell$-adic unit scaling, then they agree modulo Frobenius. The selected statement proves this uniqueness; existence of a field isomorphism for every admissible Galois-data isomorphism is outside it.

## Lean: Injectivity of Bogomolov–Pop reconstruction modulo the stated ambiguities

Stated in [BogomolovPopInjectivity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BogomolovPopInjectivity.lean).

```lean
theorem main_graph_injective (ell : ℕ) [Fact ell.Prime]
    (k K l L : Type*) [Field k] [Field K] [Field l] [Field L]
    [IsAlgClosed k] [IsAlgClosed l] [Algebra k K] [Algebra l L]
    [Algebra.EssFiniteType k K] [Algebra.EssFiniteType l L]
    (hk : (ell : k) ≠ 0) (hl : (ell : l) ≠ 0)
    (hK : 2 ≤ Algebra.trdeg k K) (hL : 2 ≤ Algebra.trdeg l L) :
    ∀ (a a' : IsomF k K l L) (b : IsomCUnits ell K L),
      PhiGraph a b → PhiGraph a' b → a = a'
```

Proved in [lean/OAI/Algebra/BogomolovPop/Injectivity.lean, line 305](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/BogomolovPop/Injectivity.lean#L305).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/009.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/009.md)
