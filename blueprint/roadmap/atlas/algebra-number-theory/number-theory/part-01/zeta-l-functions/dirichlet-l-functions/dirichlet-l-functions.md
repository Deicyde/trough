---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry18Bernoullidiff.ramanujan_part1_ch7_entry18_bernoullidiff
statement: formalized
proof: formalized
---

# Dirichlet characters and L-functions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/index.html).

Dirichlet characters, conductors, primitive and quadratic characters, Dirichlet series continuation, L-function bounds, Artin and Selberg-class functions.

## Functional equation of the Dirichlet beta function

Let $\chi$ be the non-principal
Dirichlet character modulo $4$, so $\chi(1) = 1$, $\chi(3) = -1$ and $\chi(0) = \chi(2) = 0$; let
$\beta(s) = L(s, \chi)$ be its Dirichlet $L$-function (the Dirichlet beta function, continued to
all of $\mathbb{C}$); and put $E^*(s) = 2\,\Gamma(s)\,\beta(s) / (\pi/2)^s$. Then the functions
$\cos(\pi r/2)\, E^*(1 - r)$, $(\pi/2)^r E^*(r) / \Gamma(r)$ and
$\cos(\pi r/2)\, (\pi/2)^{r-1}\, \Gamma(1 - r)\, \beta(1 - r)$ of $r \in \mathbb{C}$ are
meromorphic on $\mathbb{C}$, and outside a closed discrete subset of $\mathbb{C}$ we have
$\cos(\pi r/2)\, E^*(1 - r) = 2\beta(r) = (\pi/2)^r E^*(r) / \Gamma(r)$ and
$\beta(r) = \cos(\pi r/2)\, (\pi/2)^{r-1}\, \Gamma(1 - r)\, \beta(1 - r)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry18Bernoullidiff.ramanujan_part1_ch7_entry18_bernoullidiff`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry18Bernoullidiff.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry18Bernoullidiff.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/index.html#ramanujan-part1-ch7-entry18-bernoullidif).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dirichlet characters and L-functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions)
