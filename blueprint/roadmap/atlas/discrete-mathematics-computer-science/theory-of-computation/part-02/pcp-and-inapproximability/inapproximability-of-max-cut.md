---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCutN, MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCutFeas, MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCutVal, MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCut, MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.max_cut_no_ptas
statement: formalized
---

# Inapproximability of MAX-CUT

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut/index.html).

## Vertex count of a MAX-CUT instance

The vertex count of a MAX-CUT instance, a bitstring
$x$ of length $|x|$, is $\lfloor \sqrt{|x|} \rfloor$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCutN`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut/index.html#max-cut-n).

## Feasible MAX-CUT solutions

A bitstring $s$ is a feasible solution of a MAX-CUT instance
$x$ exactly when the length of $s$ equals the vertex count $\lfloor \sqrt{|x|} \rfloor$ of $x$,
so that $s$ has one bit per vertex.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCutFeas`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut/index.html#max-cut-feas).

## Value of a MAX-CUT solution

Let $x$ be a MAX-CUT instance with vertex count
$n = \lfloor \sqrt{|x|} \rfloor$ and let $s$ be a bitstring, with bits indexed from $0$. If $s$
is a feasible solution of $x$ (its length is $n$), the value of $s$ is the number, as a rational
number, of pairs $(i, j)$ with $i < j < n$ such that bit $i n + j$ of $x$ is true and bits $i$
and $j$ of $s$ differ; otherwise the value is $0$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCutVal`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut/index.html#max-cut-val).

## MAX-CUT as an optimization problem

MAX-CUT is the optimization problem whose instances
are bitstrings $x$, read as an adjacency matrix on $n = \lfloor \sqrt{|x|} \rfloor$ vertices in
which, for $i < j < n$, bit $i n + j$ of $x$ (bits indexed from $0$) says whether $\{i, j\}$ is
an edge. Its feasible solutions for $x$ are the bitstrings of length $n$, one bit per vertex;
the value of a feasible solution $s$ is the number of pairs $i < j < n$ that are edges and
whose bits in $s$ differ, the value of an infeasible solution is $0$, and the polynomial bound
on the length of feasible solutions is $p(m) = m$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.maxCut`, a definition declared in [WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut/index.html#max-cut).

## MAX-CUT has no PTAS unless P = NP

If $\mathsf{P} \neq \mathsf{NP}$, then the
optimization problem MAX-CUT does not admit a polynomial-time approximation scheme.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440 (MAX-CUT is MAXSNP-complete, hence APX-hard); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 11 (APX-hardness rules out a PTAS unless P = NP).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MaxCutNoPTAS.max_cut_no_ptas` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MaxCutNoPTASWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut/index.html#max-cut-no-ptas).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inapproximability of MAX-CUT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/pcp-and-inapproximability/inapproximability-of-max-cut)
