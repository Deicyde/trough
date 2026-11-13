---
declaration: section
origin: cited
lean: MetaMathlibExt.matveev_lower_bound_linear_forms_logarithms, MathlibExt.NumberTheory.SchmidtSubspaceWanted.NumberTheory.SchmidtSubspace.schmidt_subspace
statement: formalized
---

# Roth's theorem and linear forms in logarithms: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/index.html).

Thue–Siegel–Roth, Ridout, Schmidt subspace, Baker, Baker–Wüstholz, Matveev bounds, Baker–Davenport reduction, approximation by algebraic numbers.

## Matveev's lower bound for linear forms in logarithms (real case)

Let $L$ be a number
field of degree $D = [L : \mathbb{Q}]$ with a field embedding $f : L \to \mathbb{R}$, let $s \ge 1$
be a natural number, and let $\eta_1, \dots, \eta_s \in L$ satisfy $\eta_i \ne 1$ and
$f(\eta_i) > 0$ for every $i$. Let $d_1, \dots, d_s$ be nonzero integers and let $B$ be a real
number with $B \ge 1$ and $|d_i| \le B$ for every $i$. Let $A_1, \dots, A_s$ be real numbers with
$A_j \ge \max(D\,h(\eta_j), |\log f(\eta_j)|, 0.16)$ for every $j$, where $h$ is the absolute
logarithmic Weil height. Put $\Gamma = f(\eta_1)^{d_1} \cdots f(\eta_s)^{d_s} - 1$. If
$\Gamma \ne 0$, then

$$\log|\Gamma| > -1.4 \cdot 30^{s+3} \, s^{4.5} \, D^2 (1 + \log D)(1 + \log B) \, A_1 \cdots A_s.$$

No integrality is assumed on the $\eta_i$, so the statement also covers non-integral algebraic
numbers, such as the element in the source's application whose minimal polynomial has leading
coefficient $23$. The source states the bound with $B = \max_i |d_i|$; since the right-hand side
increases with $B$, any real $B \ge 1$ bounding every $|d_i|$ may be used.

## Sources

- Salah Eddine Rihane, Chèfiath Awero Adegbindin, and Alain Togbé, "Fermat Padovan And Perrin Numbers", Journal of Integer Sequences 23 (2020), Article 20.6.2, Section 2.1 and its Matveev theorem. Source URL <https://cs.uwaterloo.ca/journals/JIS/VOL23/Togbe/togbe16.tex>, definitions-and-theorem source lines 148–178, theorem lines 172–178. The source cites Bugeaud–Mignotte–Siksek, Theorem 9.4, as a modified consequence of E. M. Matveev, "An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers, II", Izv. Math. 64 (2000), 1217–1269.

Stated but not proved: `MetaMathlibExt.matveev_lower_bound_linear_forms_logarithms` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/MatveevLinearFormsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/MatveevLinearFormsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/index.html#matveev-lower-bound-linear-forms-logarit).

## Schmidt's subspace theorem

Let $\sigma$ be a finite set with at least two elements, and
for $i \in \sigma$ let $L_i(x) = \sum_{j \in \sigma} a_{ij} x_j$ be linear forms whose
coefficients $a_{ij} \in \mathbb{C}$ are algebraic over $\mathbb{Q}$ and whose coefficient
vectors $(a_{ij})_{j \in \sigma}$ are linearly independent over $\mathbb{C}$. Let
$\varepsilon > 0$ be real. Then there is a finite set $S$ of nonzero vectors in
$\mathbb{Z}^\sigma$ such that every $x \in \mathbb{Z}^\sigma$ with
$\left|\prod_{i \in \sigma} L_i(x)\right| < \|x\|^{-\varepsilon}$, where
$\|x\| = \max_{j \in \sigma} |x_j|$, satisfies $\sum_{i \in \sigma} c_i x_i = 0$ for some $c \in S$.

Every proper subspace of $\mathbb{Q}^\sigma$ lies in a hyperplane $\sum_i c_i x_i = 0$ with a
nonzero integer vector $c$, so this is the usual form: these $x$ lie in finitely many proper
subspaces.

## Sources

- W.M. Schmidt, Diophantine approximation, Lecture Notes in Mathematics 785, Springer Verlag 1980, Chap. V,VI,VII. Problem `schmidt_subspace` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.SchmidtSubspaceWanted.NumberTheory.SchmidtSubspace.schmidt_subspace` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchmidtSubspaceWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchmidtSubspaceWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/index.html#schmidt-subspace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Roth's theorem and linear forms in logarithms](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms)
