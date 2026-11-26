# OrbitalMechanics

The folder [Physlib/ClassicalMechanics/OrbitalMechanics/](https://github.com/leanprover-community/physlib/tree/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics): 1 module, with an article.

The repository's API map for this folder, *Orbital mechanics* ([Physlib/ClassicalMechanics/OrbitalMechanics/API-map.md](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### System and configuration
>
> The system is the gravitational constant G, the central mass M and the orbiting mass m, and a configuration is the orbital radius r. [\[1\]](visviva.md) The circular speed, the specific orbital energy and the escape speed use the gravitational parameter G M of the central body alone, the limit of a test body with m ≪ M; the two-body period and the reflex motion use the total mass M + m. [\[1\]](visviva.md)
>
> ### Circular orbits
>
> The circular speed at radius r is √(G M / r), with square G M / r. [\[2\]](visviva.md) It equals the radius times the circular angular rate √(G M / r³). \[3\]
>
> ### The two-body period and the reflex motion
>
> The period of a circular two-body orbit at separation r is 2π √(r³ / (G (M + m))), which satisfies Kepler's third law P² G (M + m) = 4π² r³ \{1}. [\[4\]](visviva.md) The central body circles the barycentre at distance m r / (M + m), and its reflex speed, once round that circle per period, satisfies K³ = 2π G m³ / (P (M + m)²); for a star with a planet on an edge-on circular orbit this is the radial-velocity semi-amplitude \{2}. [\[5\]](visviva.md)
>
> ### Energy and the escape speed
>
> The specific orbital energy at speed v and radius r is v² / 2 − G M / r, and on a circular orbit it is −(G M / r) / 2, half the potential energy per unit mass. [\[6\]](visviva.md) The escape speed √(2 G M / r) is positive, its square is 2 G M / r, and the specific orbital energy vanishes there. [\[7\]](visviva.md) It is √2 times the circular speed at the same radius, so a body on a circular orbit moves more slowly than the escape speed and is bound. \[8\]
>
> ### General orbits
>
> … In a planar binary, the relative displacement sweeps out equal signed areas in equal times within a collision-free interval. Its areal rate is half the signed angular momentum per unit reduced mass. \[9\] …

Its references:

> - \{1\} Landau & Lifshitz, *Mechanics*, 3rd ed., Sections 13 and 15.
> - \{2\} Perryman, *The Exoplanet Handbook*, 2nd ed., Chapter 2.

- [Vis viva for circular orbits and the escape speed](visviva.md)
