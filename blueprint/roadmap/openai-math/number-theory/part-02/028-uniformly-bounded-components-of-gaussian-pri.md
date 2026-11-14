---
declaration: section
origin: cited
lean: OAI.GaussianMoat.fullMain
statement: formalized
proof: formalized
---

# 028. Uniformly bounded components of Gaussian-prime graphs

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Gaussian moat conjecture: no infinite walk through distinct Gaussian primes can have uniformly bounded steps. More strongly, for every distance bound *D*, the graph joining Gaussian primes at distance at most *D* has uniformly bounded finite component sizes, depending only on *D*, including primes on the coordinate axes.

## Bounded-Step Walks on Gaussian Primes

We prove the Gaussian moat conjecture: no infinite walk through distinct Gaussian primes can have bounded steps. More strongly, for each fixed finite step bound, the connected components of the Gaussian-prime graph have uniformly bounded size. This bound applies to every starting prime, including primes on the coordinate axes, and is nonexplicit. The proof constructs a finite periodic sieve obstruction using geometric sampling and information-theoretic estimates.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Gaussian moat problem asks whether an infinite walk through distinct Gaussian primes can have bounded step lengths. The formalized result gives a negative answer for every real step bound $D$. More strongly, one finite bound depending only on $D$ limits the size of every connected component of the bounded-step graph and the length of every injective bounded-step walk. Axis primes and all associates are included. No explicit function of $D$ is supplied.

## Lean: Uniform bounds for bounded-step Gaussian-prime walks

```lean
theorem fullMain : MainEndpoint ∧ UniformEndpoint
```

Stated in [GaussianMoat.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GaussianMoat.lean#L36). Proved in [lean/OAI/NumberTheory/GaussianMoat/Main.lean, line 102](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/GaussianMoat/Main.lean#L102). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/028.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/028.md)
