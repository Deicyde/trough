---
declaration: section
origin: cited
lean: OAI.MatchingFPRAS.thm_main, OAI.MatchingEntropy.entropy_main, OAI.BinaryMatching.deterministic_approximate_counting, OAI.LoopMatching.fullEndpoint, OAI.MatchingEntropyBounds.Refined.pointwise_entropy, OAI.TriangleFace198.triangle_expansion_face
statement: formalized
---

# 113. Approximate counting and entropy of perfect matchings

2 manuscripts and 6 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a fully polynomial randomized approximation scheme for counting perfect matchings in arbitrary finite simple graphs, with exact detection of zero counts. Also proves the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant, bounding the maximum entropy of a matching law at every feasible edge-marginal vector in a loopless labelled multigraph, including boundary points.

## A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs

We give a fully polynomial randomized approximation scheme (FPRAS) for counting perfect matchings in arbitrary finite simple undirected graphs, resolving the general-graph perfect-matching approximation problem. The algorithm returns zero with certainty when no perfect matching exists. Otherwise, it achieves relative error *ε* with failure probability at most *δ* in worst-case bit time polynomial in the input length, $\varepsilon ^{-1}$, and $\log\delta^{-1}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf); the Lean below formalizes results from it.

## Entropy and Face Dimension of the Perfect-Matching Polytope

We prove the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant. For every feasible vector *x* of perfect-matching edge marginals in a loopless labelled multigraph on $2m\ge2$ vertices, the maximum entropy $H(x)$ of a matching law with marginals *x* satisfies

$\displaystyle F(x)-(2-2/m)B(x)\le H(x)\le F(x),$

where $F(x)=-\sum_e x_e\log x_e$ and $B(x)=-\sum_e(1-x_e)\log(1-x_e)$. This bound holds throughout the polytope, including its boundary. We also prove the sharp bound $|\mathop{\mathrm{supp}}\nolimits x|-\dim F_x\le3m-2$, where $F_{x}$ is the minimal face of the perfect-matching polytope containing *x*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives a fully polynomial randomized approximation scheme for counting perfect matchings in every finite simple undirected graph. For rational $0<\varepsilon<1$ and $0<\delta<1/2$, it returns a nonnegative rational estimate with relative error at most $\varepsilon$ with probability at least $1-\delta$. If the graph has no perfect matching, every execution returns zero.

The algorithm is a fixed finite-alphabet randomized machine. Its worst-case running time is polynomial in the binary input length, $\varepsilon^{-1}$, and $\log(\delta^{-1})$, including on unsuccessful random tapes.

For feasible edge marginals $x$ of perfect matchings in a loopless multigraph on $2m$ vertices, let $F(x)=-\sum_e x_e\log x_e$, $B(x)=-\sum_e(1-x_e)\log(1-x_e)$, and let $H(x)$ be the maximum entropy of a matching law with those marginals. The formalization proves $F(x)-(2-2/m)B(x)\le H(x)\le F(x)$ for $m\ge1$, including boundary points of the polytope. It retains the earlier coefficient-eight entropy bound and the deterministic counting approximations with factors $512^n$ for loopless graphs and $2^{18n}$ with singleton loops.

A further statement identifies the exact face obtained by expanding a degree-three vertex into a triangle and shows that minimal faces are carried to minimal faces by the expansion. The paper's sharp global face-dimension bound is not part of that selected statement.

## Lean: Randomized approximation of the perfect-matching count

```lean
theorem thm_main : MainStatement
```

Stated in [MatchingFPRAS.lean, line 105](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatchingFPRAS.lean#L105). Proved in [lean/OAI/Combinatorics/MatchingCount/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/MatchingCount/Main.lean#L21).

## Lean: Perfect-matching entropy bound

```lean
theorem entropy_main (G : LooplessGraph V E) (m : ℕ)
    (hm : 0 < m) (hV : Fintype.card V = 2 * m)
    (hPM : Nonempty G.Matching) (y : E → ℝ) (hy : y ∈ G.polytope) :
    marginalEntropy y - maxMatchingEntropy G y ≤
      8 * (m : ℝ) * (1 - Real.exp (-marginalEntropy y / (m : ℝ)))
```

Stated in [MatchingEntropy.lean, line 58](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatchingEntropy.lean#L58). Proved in [lean/OAI/Combinatorics/PerfectMatching/Main.lean, line 85](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/PerfectMatching/Main.lean#L85). formalization.yaml lists it as one of the repository's main results.

## Lean: Deterministic approximate matching count

```lean
theorem deterministic_approximate_counting :
    ∃ A : Input → ℕ,
      ∃ machine : Turing.TM2ComputableInPolyTime encodeInput Nat.bits A,
        (∀ k, Finite (machine.tm.Γ k)) ∧
        (∃ P : Polynomial ℕ, ∀ G,(A G).bits.length≤P.eval (encodeInput G).length) ∧
        ∀ G,A G≤count G ∧ count G≤2^(9*G.n)*A G ∧ (A G=0 ↔ count G=0)
```

Stated in [BinaryMatching.lean, line 66](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BinaryMatching.lean#L66). Proved in [lean/OAI/Computability/MatchingCount/BinarySolve.lean, line 143](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/MatchingCount/BinarySolve.lean#L143). formalization.yaml lists it as one of the repository's main results.

## Lean: Approximate counting with singleton loops

```lean
theorem fullEndpoint : FullEndpoint
```

Stated in [SingletonLoopMatching.lean, line 127](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SingletonLoopMatching.lean#L127). Proved in [lean/OAI/Computability/LoopMatching/Main.lean, line 24](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/LoopMatching/Main.lean#L24). formalization.yaml lists it as one of the repository's main results.

## Lean: Refined pointwise perfect-matching entropy bounds

```lean
theorem Refined.pointwise_entropy (G : LooplessGraph V E) (m : ℕ)
    (hm : 0 < m) (hV : Fintype.card V = 2 * m) (hPM : Nonempty G.Matching)
    (x : E → ℝ) (hx : x ∈ G.polytope) :
    entropy x - (2 - 2 / (m : ℝ)) * complementEntropy x ≤ maxMatchingEntropy G x ∧
      maxMatchingEntropy G x ≤ entropy x
```

Stated in [MatchingEntropyBounds.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatchingEntropyBounds.lean#L73). Its proof is in [lean/OAI/Combinatorics/MatchingEntropy/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/MatchingEntropy/Main.lean) or a file it imports further down, which this chapter does not read.

## Lean: Face correspondence under triangle expansion

```lean
theorem triangle_expansion_face {V : Type uV} {E : Type uE}
    [Fintype V] [Fintype E] [DecidableEq V] [DecidableEq E] (G : LooplessGraph V E) (v : V)
    (hdeg : Fintype.card {e : E // G.Incident v e} = 3)
    (_hmatching : Nonempty G.Matching) :
    ∃ (c : E → Fin 3) (hc : LocalLabels G v c),
      let H := triangleExpansion G c v
      let f := localExtension G c v hc
      let Q := {y | y ∈ H.polytope ∧ H.cutMass y (triangleVertices v) = 1}
      f '' G.polytope = Q ∧
      Convex ℝ Q ∧ IsExtreme ℝ H.polytope Q ∧
      (∀ x, oldRestriction (f x) = x) ∧
      (∀ y ∈ Q, f (oldRestriction y) = y) ∧
      (∀ x e, f x (Sum.inl e) = x e) ∧
      (∀ x i, f x (Sum.inr i) = x (localEdge G c v hc i)) ∧
      (∀ x, (∀ e, x e = (1/3 : ℝ)) → ∀ e, f x e = (1/3 : ℝ)) ∧
      (∀ x ∈ G.polytope, CanonicalFace198.minFace H.polytope (f x) = f '' CanonicalFace198.minFace G.polytope x)
```

Stated in [TriangleFace.lean, line 169](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TriangleFace.lean#L169). Proved in [lean/OAI/Combinatorics/TriangleFace/Main.lean, line 51](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/TriangleFace/Main.lean#L51).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/113.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/113.md)
