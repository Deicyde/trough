---
declaration: theorem
origin: cited
lean: GaloisRepresentation.IsHardlyRamified.mem_isCompatible
statement: formalized
---

# hardly_ramified_spreads_out

If $\ell\geq3$ is prime, $K$ is a finite extension of $\mathbb{Q}_\ell$ with integers $\mathcal{O}$ and if $\rho:\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to\operatorname{GL}_2(\mathcal{O})$ is a hardly ramified representation whose reduction is irreducible, then there exists a number field $M$ and, for each finite place $\mu$ of $M$ of characteristic prime to 2, with completion $M_\mu$ having integer ring $R_\mu$, a hardly ramified semisimple representation $\rho_\mu:\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to\operatorname{GL}_2(R_\mu)$ (by which we mean the generic fibre is semisimple), with the following properties:

- There is some $\lambda\mid\ell$ of $M$ such that $\rho_\lambda\cong\rho$, the isomorphism happening over some appropriate local field containing a copy of $M_\lambda$ and a copy of $K$;
- If $\mu_1$ and $\mu_2$ are two finite places of $M$ with odd residue characteristics $m_1$ and $m_2$, and if $p\nmid 2m_1m_2$ is prime, then $\rho_{\mu_1}$ and $\rho_{\mu_2}$ are both unramified at $p$ and the characteristic polynomials $\rho_{\mu_1}(\operatorname{Frob}_p)$ and $\rho_{\mu_2}(\operatorname{Frob}_p)$ lie in $M[X]$ and are equal.

## Depends on

- [hardly_ramified](hardly-ramified.md)

## Proof

Omitted for now **TODO**

## Lean

Stated as [`GaloisRepresentation.IsHardlyRamified.mem_isCompatible`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/GaloisRepresentation.IsHardlyRamified.mem_isCompatible); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch03freyreduction.tex, line 185](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch03freyreduction.tex#L185)
