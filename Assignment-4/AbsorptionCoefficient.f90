program main
    implicit none
    integer, parameter :: dp = selected_real_kind(8)
    real(dp), parameter :: Gammaba = 1.d-2, Gammaca = 1.d0, omegaca = 10.d0
    real(dp) :: Omegas, omegap, alpha

    open(unit = 1, file = 'AbsorptionCoefficient-1.txt', status = 'unknown')
    omegap = 0.d0
    Omegas = 0.d0
    do while (omegap <= 20.d0)
        alpha = omegap * ((omegap - omegaca) + Gammaba**2)**2&
        * (Gammaba * Omegas**2 + Gammaca * ((omegap - omegaca)**2 + Gammaba**2))&
        / ((omegap - omegaca)**2 * (Omegas**2 - ((omegap - omegaca)**2 + Gammaba**2))**2&
            + (Gammaba * Omegas**2 + Gammaca * ((omegap - omegaca)**2 + Gammaba**2))**2)
        write(1,'(2f20.8)') omegap / omegaca, alpha
        omegap = omegap + 1.d-2
    end do
    close(1)

    open(unit = 2, file = 'AbsorptionCoefficient-2.txt', status = 'unknown')
    omegap = 0.d0
    Omegas = .5d0 * Gammaca
    do while (omegap <= 20.d0)
        alpha = omegap * ((omegap - omegaca) + Gammaba**2)**2&
        * (Gammaba * Omegas**2 + Gammaca * ((omegap - omegaca)**2 + Gammaba**2))&
        / ((omegap - omegaca)**2 * (Omegas**2 - ((omegap - omegaca)**2 + Gammaba**2))**2&
            + (Gammaba * Omegas**2 + Gammaca * ((omegap - omegaca)**2 + Gammaba**2))**2)
        write(2,'(2f20.8)') omegap / omegaca, alpha
        omegap = omegap + 1.d-2
    end do
    close(2)

    open(unit = 3, file = 'AbsorptionCoefficient-3.txt', status = 'unknown')
    omegap = 0.d0
    Omegas = 5.d0 * Gammaca
    do while (omegap <= 20.d0)
        alpha = omegap * ((omegap - omegaca) + Gammaba**2)**2&
        * (Gammaba * Omegas**2 + Gammaca * ((omegap - omegaca)**2 + Gammaba**2))&
        / ((omegap - omegaca)**2 * (Omegas**2 - ((omegap - omegaca)**2 + Gammaba**2))**2&
            + (Gammaba * Omegas**2 + Gammaca * ((omegap - omegaca)**2 + Gammaba**2))**2)
        write(3,'(2f20.8)') omegap / omegaca, alpha
        omegap = omegap + 1.d-2
    end do
    close(3)

end program main
