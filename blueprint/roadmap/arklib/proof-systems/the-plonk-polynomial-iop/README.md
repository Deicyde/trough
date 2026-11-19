# The Plonk Polynomial IOP

ArkLib formalizes the polynomial oracle reduction underlying Plonk ([Gabizon et al. 2019](https://eprint.iacr.org/2019/953.pdf)). It composes four stages, each a standalone oracle reduction. The result concerns the polynomial IOP; it does not include a polynomial commitment scheme or Fiat–Shamir.

Fix a field $\mathbb{F}$ with decidable equality, a number of rows $n\geq 2$, and a primitive $n$-th root of unity $\omega$, so that $H=\{1,\omega,\ldots,\omega^{n-1}\}$ is the row domain. A constraint system has $m$ variables and $n$ gates; each gate constrains a left, right and output wire, and copy constraints identify wires that carry the same variable. Fix coset labels for the three wire columns and a public-input polynomial $\mathit{pi}$ of degree less than $n$. A wire table is three polynomials $a_0,a_1,a_2$ of degree less than $n$.

- [Plonk oracle reduction](def-plonk-assembly.md)
- [Plonk completeness](thm-plonk-completeness.md)
- [Plonk knowledge soundness](thm-plonk-knowledge-soundness.md)

The circuit relation. For a constraint system with $\ell\leq m$ public inputs, the Plonk relation holds for a public input $x\in\mathbb{F}^{\ell}$ and a private witness $w\in\mathbb{F}^{m-\ell}$ when the assignment $(x,w)$ satisfies every gate and copy constraint. To prove it, the constraint system is prepared: $\ell$ public-equality rows are prepended, so the domain has $\ell+n$ rows and $\omega$ is a primitive $(\ell+n)$-th root of unity with $\ell+n\geq 2$. The public constants of the new rows are cleared and $x$ enters through the public-input polynomial.

- [Plonk knowledge soundness for the circuit relation](thm-plonk-circuit-knowledge-soundness.md)
