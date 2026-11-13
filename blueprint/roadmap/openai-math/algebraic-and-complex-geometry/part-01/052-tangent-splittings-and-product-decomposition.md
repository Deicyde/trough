---
declaration: section
origin: cited
lean: OAI.UniversalCoverSplitting.main, OAI.SplitTangent.integrability_main
statement: formalized
proof: formalized
---

# 052. Tangent splittings and product decompositions

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

A splitting of the tangent bundle of a compact Kähler manifold into two integrable holomorphic subbundles induces a compatible product decomposition of its universal cover, proving the two-summand form of Beauville's splitting conjecture. On smooth rationally connected projective manifolds, both summands are automatically integrable, establishing Höring's conjecture and the corresponding product decomposition.

## Universal-cover splitting for compact Kähler manifolds

We prove the two-summand form of Beauville's compatible splitting conjecture. If the tangent bundle of a compact connected Kähler manifold decomposes into two integrable holomorphic subbundles of positive rank, then its ordinary universal cover admits a product decomposition whose factor tangent bundles are the lifted specified summands.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Integrability of split tangent bundles on rationally connected manifolds

We prove that both summands of every specified holomorphic splitting of the tangent bundle of a smooth rationally connected projective complex manifold into two positive-rank subbundles are integrable. This proves Höring's conjecture on rationally connected projective manifolds. Höring's product theorem then gives a product decomposition compatible with the specified splitting.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The splitting question asks whether a holomorphic decomposition of the tangent bundle comes from a product decomposition of the universal cover. The formalized result gives an affirmative answer for a compact connected Kähler manifold whose tangent bundle splits into two positive-rank, integrable holomorphic subbundles. The universal cover is a product of connected simply connected complex manifolds of the prescribed dimensions, and the differential identifies the two tangent factors with the original summands.

Both integrability assumptions are required. Automatic integrability and the paper's additional corollaries are not included.

The formalization proves integrability of both summands in a holomorphic splitting of the tangent bundle of a rationally connected projective manifold. More precisely, for a compact connected complex manifold of dimension at least two with a projective embedding witnessing rational connectedness, each positive-rank summand of a holomorphic tangent-bundle splitting is integrable. The paper's compatible product decomposition is a separate consequence, outside this selected statement.

## Lean: Universal-cover product splitting

```lean
theorem main (X : ComplexManifold.{u} n) [CompactSpace X.Carrier]
    [ConnectedSpace X.Carrier] (hn : 2 ≤ n) (hr₁ : 0 < r₁) (hr₂ : 0 < r₂)
    (g : KahlerMetric X) (S : HolomorphicSplitting X r₁ r₂)
    (h₁ : Integrable S.projection) (h₂ : Integrable (complementaryProjection S))
    (Z : ComplexManifold.{v} n) (π : OrdinaryUniversalCover X Z) :
    ∃ (Y₁ : ComplexManifold.{v} r₁) (Y₂ : ComplexManifold.{v} r₂),
      ConnectedSpace Y₁.Carrier ∧ ConnectedSpace Y₂.Carrier ∧
      SimplyConnectedSpace Y₁.Carrier ∧ SimplyConnectedSpace Y₂.Carrier ∧
      CompatibleProduct S π Y₁ Y₂
```

Stated in [KahlerSplitting.lean, line 124](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KahlerSplitting.lean#L124). Proved in [lean/OAI/Geometry/KahlerSplitting/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/KahlerSplitting/Main.lean#L14). formalization.yaml lists it as one of the repository's main results.

## Lean: Integrability of both holomorphic tangent summands

```lean
theorem integrability_main : IntegrabilityStatement.{u}
```

Stated in [SplitTangentIntegrability.lean, line 135](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SplitTangentIntegrability.lean#L135). Proved in [lean/OAI/Geometry/SplitTangent/RationalVariation.lean, line 188](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/SplitTangent/RationalVariation.lean#L188).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/052.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/052.md)
