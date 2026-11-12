---
declaration: section
origin: cited
lean: OAI.Problem346.canonical_foulkes_howe_surjective
statement: formalized
proof: formalized
---

# 210. Foulkes' conjecture for sixth powers and quadratic stabilization

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the sixth case of Foulkes’ conjecture: $\mathop{\mathrm{Sym}}\nolimits ^6(\mathop{\mathrm{Sym}}\nolimits ^bV)$ embeds equivariantly in $\mathop{\mathrm{Sym}}\nolimits ^b(\mathop{\mathrm{Sym}}\nolimits ^6V)$ for every *b* ≥ 6 and finite-dimensional complex *V*. More generally, the canonical multiplication map $\mathop{\mathrm{Sym}}\nolimits ^b(\mathop{\mathrm{Sym}}\nolimits ^aV)\to\mathop{\mathrm{Sym}}\nolimits ^a(\mathop{\mathrm{Sym}}\nolimits ^bV)$ is surjective for *a* ≥ 2 and $b\ge a(a-1)$, giving dimension-independent quadratic stabilization.

## Foulkes' conjecture for the sixth symmetric power

We prove the sixth-symmetric-power case of Foulkes' conjecture. For every integer *b* ≥ 6 and every finite-dimensional complex vector space *V*, there is a $\mathop{\mathrm{GL}}\nolimits (V)$-equivariant injection $\mathop{\mathrm{Sym}}\nolimits ^6(\mathop{\mathrm{Sym}}\nolimits ^b V)\hookrightarrow\mathop{\mathrm{Sym}}\nolimits ^b(\mathop{\mathrm{Sym}}\nolimits ^6 V)$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/main.pdf).

## Quadratic stabilization of the canonical Foulkes--Howe map

For every finite-dimensional complex vector space *V*, we prove that the canonical Foulkes–Howe map $\mathop{\mathrm{Sym}}\nolimits ^b(\mathop{\mathrm{Sym}}\nolimits ^a V)\longrightarrow\mathop{\mathrm{Sym}}\nolimits ^a(\mathop{\mathrm{Sym}}\nolimits ^b V)$ is surjective whenever *a* ≥ 2 and $b\ge a(a-1)$. This gives a quadratic stabilization bound independent of $\dim V$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves surjectivity of the canonical averaged Foulkes–Howe map $\mathrm{Sym}^b(\mathrm{Sym}^a\,V)\to\mathrm{Sym}^a(\mathrm{Sym}^b\,V)$ for every finite-dimensional complex vector space, $a\ge2$, and $b\ge a(a-1)$. It also covers the bijective $a=1$ case, the vanishing-on-products consequence, and the corresponding equivariant embedding in the reverse direction. The sixth-power specialization is covered for $b\ge30$; the companion's full range $b\ge6$ is not included.

## Lean: Quadratic stabilization of the canonical Foulkes–Howe map

Stated in [FoulkesHowe.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FoulkesHowe.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem canonical_foulkes_howe_surjective :
    ∀ (V : Type u) [AddCommGroup V] [Module ℂ V] [FiniteDimensional ℂ V] (a b : ℕ), 2 ≤ a → a * (a - 1) ≤ b → ∃ μ : SymPow b (SymPow a V) →ₗ[ℂ] SymPow a (SymPow b V), IsFoulkesMap a b V μ ∧ Function.Surjective μ ∧ ∀ ν : SymPow b (SymPow a V) →ₗ[ℂ] SymPow a (SymPow b V), IsFoulkesMap a b V ν → ν = μ
```

Proved in [lean/OAI/RepresentationTheory/FoulkesHowe/Stabilization.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/FoulkesHowe/Stabilization.lean#L15).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/210.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/210.md)
