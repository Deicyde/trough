---
declaration: section
origin: cited
lean: OAI.CriticalZ3.critical_no_infinite, OAI.CriticalPercolation.BondGraph.no_percolation_at_criticality
statement: formalized
proof: formalized
---

# 213. Critical percolation on every quasi-transitive graph

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the Benjamini–Schramm criticality conjecture for bond percolation on every infinite connected locally finite quasi-transitive graph with $p_c\lt 1$: at the critical probability, there is almost surely no infinite cluster. The family also establishes this conclusion for both nearest-neighbor bond and site percolation on ℤ$^{3}$.

## Critical bond and site percolation on the cubic lattice

We prove that nearest-neighbor Bernoulli bond and site percolation on ℤ$^{3}$ have no infinite cluster at their respective critical parameters. The proof combines a finite connection inequality for independent hyperedges with a finite-scale extension estimate and an adaptive exploration.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## No percolation at criticality on quasi-transitive graphs

We prove that critical Bernoulli bond percolation has no infinite cluster on any infinite connected locally finite quasi-transitive graph with critical probability less than one. This resolves the bond form of the criticality conjecture of Benjamini and Schramm.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The critical-percolation question asks whether an infinite cluster can remain at the threshold. The formalized result proves that, at their respective critical probabilities, nearest-neighbor bond and site percolation on $\mathbb Z^3$ almost surely have no infinite cluster. Equivalently, almost surely every vertex belongs to a finite cluster in each model.

The formalization proves absence of an infinite cluster at criticality for Bernoulli bond percolation on every infinite connected locally finite quasi-transitive graph with critical probability $p_c<1$. At $p=p_c$, the probability that any infinite cluster exists is zero. The graph model permits bond multiplicities.

## Lean: No infinite critical clusters on $\mathbb Z^3$

Stated in [CriticalZ3.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CriticalZ3.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem critical_no_infinite :
    (∀ᵐ ω ∂bondLaw bondCritical, ∀ x : Vertex, (bondCluster ω x).Finite) ∧
    (∀ᵐ ω ∂siteLaw siteCritical, ∀ x : Vertex, (siteCluster ω x).Finite)
```

Proved in [lean/OAI/Probability/CriticalZ3/Main.lean, line 107](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/CriticalZ3/Main.lean#L107).

## Lean: No infinite cluster at the critical probability

Stated in [CriticalPercolation.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CriticalPercolation.lean).

```lean
theorem no_percolation_at_criticality [Infinite V]
    (hconnected : G.fullGraph.Connected)
    (hlocal : G.LocallyFinite)
    (hquasi : G.QuasiTransitive)
    (hpc : G.criticalProbability < 1) :
    G.law G.criticalProbability G.percolates = 0
```

Proved in [lean/OAI/Probability/CriticalPercolation/Main.lean, line 190](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/CriticalPercolation/Main.lean#L190).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/213.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/213.md)
