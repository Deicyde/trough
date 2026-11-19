---
declaration: theorem
origin: cited
lean: KummerCriterion.cyclotomicUnitIndex_primeConductor_pPrimary
statement: formalized
proof: formalized
---

# sinnott-index-pprimary

For every odd prime conductor,

$$
p\mid[(\mathcal O_{K^+})^\times:C^+_{\mathrm{norm}}]
\Longleftrightarrow
p\mid h^+(K).
$$

## Depends on

- [index-pprimary-aux](thm-index-pprimary-aux.md)

## Proof

For $p=3$ the field $K^+$ is $\mathbb{Q}$: the normalised subgroup is the whole unit group $\{\pm1\}$ and $h^+=1$, so both sides are false. For $p\ge5$ this is [Theorem index-pprimary-aux](thm-index-pprimary-aux.md).

## Lean

Formalized as [`KummerCriterion.cyclotomicUnitIndex_primeConductor_pPrimary`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.cyclotomicUnitIndex_primeConductor_pPrimary).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 447](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L447)
